from django.db import models
from datetime import date, datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.text import slugify

# Each blog post must have a title, a subtitle, author, post date, and the
# post content itself

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Cs50gPost(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(blank=True, null=True, max_length=200)
	blurb = models.TextField(blank=True, null=True)
	body = models.TextField()
	date = models.DateField(default=date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	featured = models.BooleanField(default=False)
	categories = models.ManyToManyField(Category, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

	def is_featured(self):
		return self.featured

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.title)

			has_slug = Cs50gPost.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.title) + '-' + str(count)
				has_slug = Cs50gPost.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Cs50gPost, related_name='comments', 
			on_delete=models.CASCADE)
	parent = models.ForeignKey('self', null=True, related_name='replies', 
			on_delete=models.CASCADE, blank=True)
	body = models.CharField(max_length=500)
	created = models.DateTimeField(default=now)