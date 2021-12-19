from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class TechTag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class TechPost(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(blank=True, null=True, max_length=200)
	# body = models.TextField()
	body = RichTextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	featured = models.BooleanField(default=False)
	tech_tags = models.ManyToManyField(TechTag, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

	def is_featured(self):
		return self.featured

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.title)

			has_slug = TechPost.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.title) + '-' + str(count)
				has_slug = TechPost.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)
