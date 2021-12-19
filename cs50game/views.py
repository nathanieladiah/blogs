from random import randint

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Comment, Cs50gPost
from . forms import PostForm

# Create your views here.
def index(request):
	# featured_count = Cs50gPost.objects.filter(featured=True).count()
	# need to check if there are any posts first
	featured_posts = Cs50gPost.objects.filter(featured=True)
	count = len(featured_posts)
	featured_post = featured_posts[randint(0, count-1)]

	posts = Cs50gPost.objects.all().order_by('-date')

	paginator = Paginator(posts, 4)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context = {'posts': posts, 'featured_post': featured_post}

	return render(request, 'cs50game/index.html', context)

def post(request, slug):
	post = Cs50gPost.objects.get(slug=slug)

	return render(request, 'cs50game/post.html', {
		'post': post
	})

def random(request):
	count = Cs50gPost.objects.count()
	random_post = Cs50gPost.objects.all()[randint(0, count-1)]

	return HttpResponseRedirect(reverse("cs50game:post", args=(random_post.slug,)))

def categories(request, category):
	posts = Cs50gPost.objects.filter(categories__name=category)

	paginator = Paginator(posts, 6)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts': posts, 'category': category}
	return render(request, 'cs50game/categories.html', context)

def search(request):
	query = request.GET.get('q')
	if query:
		# There was a query entered.
		results = Cs50gPost.objects.filter(title__icontains=query)
	else:
		# No query entered, return all objects
		results = Cs50gPost.objects.all()

	paginator = Paginator(results, 6)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context = {'posts': posts}

	return render(request, 'cs50game/search_results.html', context)

@user_passes_test(lambda u: u.is_superuser)
def new_post(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid:
			post = form.save(commit=False)
			post.author = request.user
			post.save()

			return redirect('cs50game:index')

	context = {'form': form}
	return render(request, 'cs50game/post_form.html', context)

@user_passes_test(lambda u: u.is_superuser)
def edit_post(request, slug):
	post = Cs50gPost.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid:
			form.save()

			return redirect('cs50game:index')

	context = {'form': form}
	return render(request, 'cs50game/post_form.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, slug):
	post = Cs50gPost.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('cs50game:index')

	context = {'item': post}
	return render(request, 'cs50game/delete.html', context)

@login_required
def comment(request, slug):
	if request.method == 'POST':
		user = request.user
		body = request.POST['body']
		post = Cs50gPost.objects.get(slug=slug)

		comment = Comment(user=user, body=body, post=post)
		comment.save() 
		return HttpResponseRedirect(reverse('cs50game:post', args=(slug, )))