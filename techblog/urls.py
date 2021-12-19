from django.urls import path
from . import views

app_name = 'techblog'
urlpatterns = [
	path("", views.index, name="index"),
	path("post/<slug:slug>/", views.post, name="post"),
	path("random/", views.random, name="random"),

	# Search paths
	path("search/", views.search, name="search"),
	path("categories/<str:category>/", views.categories, name="categories"),

	# CRUD paths
	path("new/", views.new_post, name="new_post"),
	path("edit/<slug:slug>/", views.edit_post, name="edit_post"),
]