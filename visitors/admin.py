from django.contrib import admin
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple

from . models import VisitorTag, VisitorPost

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('headline', 'featured', 'top_featured', 'created')
	list_filter = ('featured', 'top_featured', 'tags')
	fields = ('headline', 'sub_headline', ('thumbnail', 'coverpic'),
		'body', ('featured', 'top_featured'), 'slug', 'tags'
	)
	filter_horizontal = ('tags',)

admin.site.register(VisitorTag)
admin.site.register(VisitorPost, PostAdmin)