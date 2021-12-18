from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
	path("", views.index, name="index"),
	path("post/<slug:slug>", views.post, name="post"),
	path("random", views.random, name="random"),

	# CRUD PATHS
	path("new", views.new_post, name="new_post"),
	path("edit/<slug:slug>/", views.editPost, name="edit_post"),
	path("delete/<slug:slug>/", views.deletePost, name="delete_post"),
]