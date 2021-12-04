from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("post/<int:post_id>", views.post, name="post"),
	path("about", views.about, name="about"),
	path("contact", views.contact, name="contact"),
	path("random", views.random, name="random"),
	path("new", views.new_post, name="new_post"),
]