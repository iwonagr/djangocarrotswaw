from django.db import models

# Create your models here.
class Post(models.Model):
	title =  models.CharField(max_length=200)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	draft =  models.BooleanField(default=True)
	publication_date = models.DateTimeField(null=True)

class Comments(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=200)
	content = models.TextField()
	publication_date = models.DateTimeField(auto_now_add=True)
