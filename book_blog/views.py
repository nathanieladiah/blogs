from random import randint
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-created').all()
	paginator = Paginator(posts, 5)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, "book_blog/index.html", {
		'page_obj': page_obj
	})

def post(request, slug):
	post = Post.objects.get(slug=slug)

	return render(request, "book_blog/post.html", {
		'post': post
	})

def random(request):
	count = Post.objects.count()
	random_post = Post.objects.all()[randint(0, count-1)]

	return HttpResponseRedirect(reverse("book:post", args=(random_post.slug,)))

# @user_passes_test(lambda u: u.is_superuser)
# def new_post(request):
# 	if request.method == 'POST':
# 		title = request.POST['title']
# 		subtitle = request.POST['subtitle']
# 		body = request.POST['body']
# 		author = request.user

# 		post = Post(title=title, subtitle=subtitle, body=body, author=author)
# 		post.save()
# 		return HttpResponseRedirect(reverse('book:index'))

# 	return render(request, "book_blog/new_post.html")

# CRUD VIEWS

@user_passes_test(lambda u: u.is_superuser)
def new_post(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid:
			# form.save()
			post = form.save(commit=False)
			post.author = request.user
			post.save()

			return redirect('book:index')

	context = {'form': form}
	return render(request, 'book_blog/post_form.html', context)

@user_passes_test(lambda u: u.is_superuser)
def editPost(request, slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid:
			form.save()
			return redirect('book:index')

	context = {'form': form}
	return render(request, 'book_blog/post_form.html', context)

@user_passes_test(lambda u: u.is_superuser)
def deletePost(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('book:index')

	context = {'item': post}
	return render(request, 'book_blog/delete.html', context)