from django import forms
from django.forms import ModelForm

from .models import TechPost

class TechPostForm(ModelForm):

	class Meta:
		model = TechPost
		fields = ['title', 'subtitle', 'coverpic', 'featured', 'body', 
		'tech_tags']

		widgets = {
			'tech_tags':forms.CheckboxSelectMultiple()
		}