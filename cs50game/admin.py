from django.contrib import admin

from .models import Cs50gPost, Comment

# Register your models here.

admin.site.register(Cs50gPost)
admin.site.register(Comment)