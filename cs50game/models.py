from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Each blog post must have a title, a subtitle, author, post date, and the
# post content itself

class CS50GPost(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateField(default=date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def is_featured(self):
		return self.featured