from random import randint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test

from .models import Cs50gPost

# Create your views here.
def index(request):
	featured_post = Cs50gPost.objects.filter(featured=True).order_by('-featured').first()
	posts = Cs50gPost.objects.order_by('-date').all()

	paginator = Paginator(posts, 4)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'cs50game/index.html', {
		'featured_post': featured_post,
		'page_obj': page_obj
	})

def post(request, post_id):
	post = Cs50gPost.objects.get(pk=post_id)

	return render(request, 'cs50game/post.html', {
		'post': post
	})

def random(request):
	count = Cs50gPost.objects.count()
	random_post = Cs50gPost.objects.all()[randint(0, count-1)]

	return HttpResponseRedirect(reverse("cs50game-post", args=(random_post.id,)))

@user_passes_test(lambda u: u.is_superuser)
def new_post(request):
	if request.method == 'POST':
		title = request.POST['title']
		subtitle = request.POST['subtitle']
		blurb = request.POST['blurb']
		body = request.POST['body']
		coverpic = request.POST['coverpic']
		author = request.user

		# if request.POST['featured']:
		# 	featured = request.POST['featured']
		# 	print(featured)

		try:
			featured = request.POST['featured']
		except:
			featured = False

		# print(featured)

		post = Cs50gPost(title=title, subtitle=subtitle, body=body, 
			author=author, blurb=blurb, coverpic=coverpic)
		post.save()
		if featured:
			post.featured = True
			post.save()
		return HttpResponseRedirect(reverse('cs50game-index'))

	return render(request, "cs50game/new_post.html")