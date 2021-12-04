from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def register(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']

		# Ensure password matches confirmation
		password = request.POST['password']
		confirmation = request.POST['confirmation']
		if password != confirmation:
			return render(request, "authapp/register.html", {
				"message": "Passwords must match."
			})

		# Attempt to create new user
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
		except IntegrityError:
			return render(request, "authapp/register.html", {
				"message": "Username already taken."
			})
		login(request, user)
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, "authapp/register.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))