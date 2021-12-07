from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="cs50game-index"),
	path("post/<int:post_id>", views.post, name="cs50game-post"),
	# path("random", views.random, name="cs50game-random"),
	# path("new", views.new_post, name="cs50game-new_post"),
]