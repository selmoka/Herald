from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User, on_delete=models.CASCADE,default=2)
	def __str__(self):
		return self.name

class Visitor(models.Model):
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
# class User(models.Model):
# 	name = models.CharField(max_length=50)
# 	def __str__(self):
# 		return self.name
# user1 = User.objects.create_user('a5', 'lennon@thebeatles.com', 'a')
# user1.save()

class Article(models.Model):
	article_text = models.CharField(max_length=200)
	title_text = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	author_article = models.ForeignKey(Author, on_delete=models.CASCADE)
	def __str__(self):
		return self.title_text

class Comment(models.Model):
	comment_text = models.TextField(blank=True,null=True)
	pub_date = models.DateTimeField(blank=True,null=True)
	# user_comment = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	visitor_comment = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=True, 
		blank=True, default=None)
	article_comment = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.user_comment
