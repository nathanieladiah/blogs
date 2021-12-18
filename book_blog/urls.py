from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
	path("", views.index, name="index"),
	path("post/<slug:slug>", views.post, name="post"),
	path("random", views.random, name="random"),
	path("new", views.new_post, name="new_post"),
]