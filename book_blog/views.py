from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-date').all()

	return render(request, "book_blog/index.html", {
		'posts': posts
	})

def post(request, post_id):
	post = Post.objects.get(pk=post_id)

	return render(request, "book_blog/post.html", {
		'post': post
	})