from django.contrib import admin

from .models import TechPost, TechTag

# Register your models here.
@admin.register(TechPost)
class TechPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'subtitle', 'featured', 'created')
	filter_horizontal = ('tech_tags',)

admin.site.register(TechTag)