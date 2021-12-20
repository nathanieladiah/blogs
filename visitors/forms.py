from django import forms
from django.forms import ModelForm

from .models import VisitorPost

class PostForm(ModelForm):

	class Meta:
		model = VisitorPost
		fields = ['headline', 'sub_headline', 'thumbnail', 'coverpic', 
		'featured', 'top_featured', 'body', 'tags']	

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}