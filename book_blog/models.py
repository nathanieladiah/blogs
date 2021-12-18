from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

# Each blog post must have a title, a subtitle, author, post date, and the
# post content itself

class Post(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.title)

			has_slug = Post.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.title) + '-' + str(count)
				has_slug = Post.objects.filter(slug=slug).exists()
			
			self.slug = slug
		
		super().save(*args, **kwargs)