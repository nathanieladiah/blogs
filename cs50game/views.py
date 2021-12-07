from django.shortcuts import render
from .models import Cs50gPost

# Create your views here.
def index(request):
	featured_post = Cs50gPost.objects.filter(featured=True).order_by('-featured').first()
	posts = Cs50gPost.objects.filter(featured=False).all()
	return render(request, 'cs50game/index.html', {
		'featured_post': featured_post,
		'posts': posts
	})

def post(request):
	return render(request, 'cs50game/post.html')