from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class VisitorTag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class VisitorPost(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	thumbnail = models.URLField(blank=True, null=True)
	body = RichTextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	featured = models.BooleanField(default=False)
	top_featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(VisitorTag, null=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.headline

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = VisitorPost.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count)
				has_slug = VisitorPost.objects.filter(slug=slug).exists()
			
			self.slug = slug

		super().save(*args, **kwargs)

