from django.contrib import admin

from .models import Cs50gPost, Comment

# Register your models here.
class Cs50gPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'subtitle', 'featured')

admin.site.register(Cs50gPost, Cs50gPostAdmin)
admin.site.register(Comment)