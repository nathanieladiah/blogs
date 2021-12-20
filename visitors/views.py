import random
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import VisitorPost
# from .forms import PostForm
# from .filters import PostFilter

# Create your views here.
def index(request):
	posts = VisitorPost.objects.all().order_by('-created')

	featured_count = VisitorPost.objects.filter(featured=True).count()
	featured = []

	if featured_count > 0:
		randoms = random.sample(range(0, featured_count), 2)

		featured_posts = VisitorPost.objects.filter(featured=True)
		for i in randoms:
			featured.append(featured_posts[i])

	top_featured = VisitorPost.objects.filter(top_featured=True).order_by('-created').first()

	page = request.GET.get('page')
	paginator = Paginator(posts, 1)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	if featured:
		context= {'posts': posts, 'featured': featured, 'top_featured': top_featured}
	else:
		context = {'posts': posts, 'top_featured': top_featured}

	return render(request, 'visitors/index.html', context)

# def post(request, slug):
# 	post = Post.objects.get(slug=slug)

# 	context = {'post': post}
# 	return render(request, 'blog/post.html', context)

# def posts(request):
# 	posts = Post.objects.all().order_by('-created')
# 	myFilter = PostFilter(request.GET, queryset=posts)
# 	posts = myFilter.qs

# 	page = request.GET.get('page')
# 	paginator = Paginator(posts, 10)

# 	try:
# 		posts = paginator.page(page)
# 	except PageNotAnInteger:
# 		posts = paginator.page(1)
# 	except EmptyPage:
# 		posts = paginator.page(paginator.num_pages)

# 	context = {'posts': posts, 'myFilter': myFilter}
# 	return render(request, 'blog/posts.html', context)

# # CRUD VIEWS

# @login_required(login_url='index')
# def createPost(request):
# 	form = PostForm()

# 	if request.method == 'POST':
# 		form = PostForm(request.POST)
# 		if form.is_valid:
# 			form.save()

# 			return redirect('index')

# 	context = {'form': form}
# 	return render(request, 'blog/post_form.html', context)

# @login_required(login_url='index')
# def updatePost(request, slug):
# 	post = Post.objects.get(slug=slug)
# 	form = PostForm(instance=post)

# 	if request.method == 'POST':
# 		form = PostForm(request.POST, instance=post)
# 		if form.is_valid:
# 			form.save()
# 			return redirect('index')

# 	context = {'form': form}
# 	return render(request, 'blog/post_form.html', context)

# @login_required(login_url='index')
# def deletePost(request, slug):
# 	post = Post.objects.get(slug=slug)

# 	if request.method == 'POST':
# 		post.delete()
# 		return redirect('index')
	
# 	context = {'item': post}
# 	return render(request, 'blog/delete.html', context)