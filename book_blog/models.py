from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

# Each blog post must have a title, a subtitle, author, post date, and the
# post content itself

class Post(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=200)
	date = models.DateField(default=date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	body = models.TextField()

	def __str__(self):
		return self.title