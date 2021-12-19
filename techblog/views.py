from random import randint
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import TechPost
from .forms import TechPostForm

# Create your views here.
def index(request):
	return render(request, 'techblog/index.html')


def index(request):
	# In this blog 1 post will be featured at a time
	featured_post = TechPost.objects.filter(featured=True).first()

	posts = TechPost.objects.all().order_by('-created')
	paginator = Paginator(posts, 4)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context = {'posts': posts, 'featured_post': featured_post}
	return render(request, 'techblog/index.html', context)


def post(request, slug):
	post = TechPost.objects.get(slug=slug)

	context={'post': post}
	return render(request, 'techblog/post.html', context)


def random(request):
	count = TechPost.objects.count()
	random_post = TechPost.objects.all()[randint(0, count-1)]

	return redirect('techblog:post', random_post.slug)
	# return HttpResponseRedirect(reverse("cs50game:post", args=(random_post.slug,)))


def search(request):
	query = request.GET.get('q')
	if query:
		results = TechPost.objects.filter(title__icontains=query)
	else:
		results = TechPost.objects.all()

	paginator = Paginator(results, 6)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context = {'posts': posts, 'query':query}
	return render(request, 'techblog/search_results.html', context)


def categories(request, category):
	posts = TechPost.objects.filter(tech_tags__name=category)

	paginator = Paginator(posts, 6)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts': posts, 'query': category}
	return render(request, 'techblog/search_results.html', context)


# CRUD VIEWS

@user_passes_test(lambda u: u.is_superuser)
def new_post(request):
	form = TechPostForm()

	if request.method == 'POST':
		form = TechPostForm(request.POST)
		if form.is_valid:
			post = form.save(commit=False)
			post.author = request.user
			post.save()

			return redirect('techblog:index')

	context = {'form': form}
	return render(request, 'techblog/post_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_post(request, slug):
	post = TechPost.objects.get(slug=slug)
	form = TechPostForm(instance=post)

	if request.method == 'POST':
		form = TechPostForm(request.POST, instance=post)
		if form.is_valid:
			form.save()

			return redirect('techblog:index')

	context = {'form': form}
	return render(request, 'techblog/post_form.html', context)