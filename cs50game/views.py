from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Cs50gPost

# Create your views here.
def index(request):
	featured_post = Cs50gPost.objects.filter(featured=True).order_by('-featured').first()
	posts = Cs50gPost.objects.filter(featured=False).all()

	paginator = Paginator(posts, 4)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'cs50game/index.html', {
		'featured_post': featured_post,
		'page_obj': page_obj
	})

def post(request):
	return render(request, 'cs50game/post.html')