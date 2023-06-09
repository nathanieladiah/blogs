from django.shortcuts import render, redirect
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
		return HttpResponseRedirect(reverse('portfolio:index'))
	else:
		return render(request, "authapp/register.html")

def login_view(request):
	if request.method == 'POST':

		# Attempt to sign user in
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		next_value = request.POST.get('next')
		print(next_value)

		# check if authentication is successful
		if user is not None:
			login(request, user)
			if next_value == "":
				return HttpResponseRedirect(reverse('portfolio:index'))
			else:
				return redirect(next_value)
		else:
			return render(request, 'authapp/login.html', {
				"message": "Invalid username and/or password."
			})
	
	else:
		return render(request, "authapp/login.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('portfolio:index'))