from django.urls import path

from . import views

app_name = 'visitors'
urlpatterns = [
	path('', views.index, name="index"),
	path('posts/', views.posts, name="posts"),
	path('categories/<str:category>/', views.categories, name="categories"),
	path('post/<slug:slug>/', views.post, name="post"),

	# CRUD PATHS
	path('create_post/', views.createPost, name="create_post"),
	path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
	# path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),
]