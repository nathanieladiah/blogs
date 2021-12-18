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

def post(request, post_id):
	post = Cs50gPost.objects.get(pk=post_id)

	return render(request, 'cs50game/post.html', {
		'post': post
	})

def random(request):
	count = Cs50gPost.objects.count()
	random_post = Cs50gPost.objects.all()[randint(0, count-1)]

	return HttpResponseRedirect(reverse("cs50game:post", args=(random_post.id,)))

# @user_passes_test(lambda u: u.is_superuser)
# def new_post(request):
# 	if request.method == 'POST':
# 		title = request.POST['title']
# 		subtitle = request.POST['subtitle']
# 		blurb = request.POST['blurb']
# 		body = request.POST['body']
# 		coverpic = request.POST['coverpic']
# 		author = request.user

# 		# if request.POST['featured']:
# 		# 	featured = request.POST['featured']
# 		# 	print(featured)

# 		try:
# 			featured = request.POST['featured']
# 		except:
# 			featured = False

# 		# print(featured)

# 		post = Cs50gPost(title=title, subtitle=subtitle, body=body, 
# 			author=author, blurb=blurb, coverpic=coverpic)
# 		post.save()
# 		if featured:
# 			post.featured = True
# 			post.save()
# 		return HttpResponseRedirect(reverse('cs50game:index'))

# 	return render(request, "cs50game/new_post.html")

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

@login_required
def comment(request, post_id):
	if request.method == 'POST':
		user = request.user
		body = request.POST['body']
		post = Cs50gPost.objects.get(pk=post_id)

		comment = Comment(user=user, body=body, post=post)
		comment.save() 
		return HttpResponseRedirect(reverse('cs50game:post', args=(post_id, )))