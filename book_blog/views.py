from random import randint
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-date').all()
	paginator = Paginator(posts, 5)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, "book_blog/index.html", {
		'page_obj': page_obj
	})

def post(request, post_id):
	post = Post.objects.get(pk=post_id)

	return render(request, "book_blog/post.html", {
		'post': post
	})

def about(request):
	return render(request, "book_blog/about.html")

def contact(request):
	return render(request, "book_blog/contact.html")

def random(request):
	count = Post.objects.count()
	random_post = Post.objects.all()[randint(0, count-1)]

	return HttpResponseRedirect(reverse("post", args=(random_post.id,)))