from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-date').all()

	return render(request, "book_blog/index.html", {
		'posts': posts
	})