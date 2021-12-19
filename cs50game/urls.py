from django.urls import path
from . import views

app_name = 'cs50game'
urlpatterns = [
	path("", views.index, name="index"),
	path("post/<int:post_id>", views.post, name="post"),
	path("random", views.random, name="random"),

	# CRUD Paths
	path("new", views.new_post, name="new_post"),
	path("comment/<int:post_id>", views.comment, name="comment"),
	path("edit/<slug:slug>/", views.edit_post, name="edit_post"),
	path("delete/<slug:slug>/", views.delete_post, name="delete_post"),
]