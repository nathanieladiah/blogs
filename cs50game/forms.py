from django import forms
from django.forms import ModelForm

from . models import Cs50gPost

class PostForm(ModelForm):

	class Meta:
		model = Cs50gPost
		# fields = '__all__'
		fields = ['title', 'subtitle', 'coverpic', 'featured', 'blurb', 'body']
