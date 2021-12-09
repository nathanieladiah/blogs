from django.db import models
from datetime import date, datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

# Each blog post must have a title, a subtitle, author, post date, and the
# post content itself

class Cs50gPost(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=200)
	blurb = models.TextField()
	body = models.TextField()
	date = models.DateField(default=date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def is_featured(self):
		return self.featured

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Cs50gPost, related_name='comments', 
			on_delete=models.CASCADE)
	parent = models.ForeignKey('self', null=True, related_name='replies', 
			on_delete=models.CASCADE, blank=True)
	body = models.CharField(max_length=500)
	created = models.DateTimeField(default=now)