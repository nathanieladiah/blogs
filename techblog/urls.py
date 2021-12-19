from django.urls import path
from . import views

app_name = 'techblog'
urlpatterns = [
	path("", views.index, name="index"),
]