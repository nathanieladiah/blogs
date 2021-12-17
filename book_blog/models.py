from django.db import models
from datetime import date
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

# Each blog post must have a title, a subtitle, author, post date, and the
# post content itself

class Post(models.Model):
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=200)
	date = models.DateField(default=date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coverpic = models.URLField(blank=True, null=True)
	body = RichTextField(null=True, blank=True)

	def __str__(self):
		return self.title