from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'subtitle', 'created')

admin.site.register(Post, PostAdmin)