from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("post/<int:post_id>", views.post, name="post"),
	path("random", views.random, name="random"),
	path("new", views.new_post, name="new_post"),
]