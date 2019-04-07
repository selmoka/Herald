from random import randint
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fnews.settings')

import django
django.setup()

from herald.models import Article, Comment, Author, Visitor
from faker import Faker
from django.contrib.auth.models import User

# article_text = models.CharField(max_length=200)
# 	title_text = models.CharField(max_length=50)
# 	pub_date = models.DateTimeField('date published')
# 	author_article = models.ForeignKey(Author, on_delete=models.CASCADE)

# class Author(models.Model):
# 	name = models.CharField(max_length=50)
# 	def __str__(self):
# 		return self.name

if __name__ == '__main__':
	print('Starting to populate...')
    # call your script's functions here
	print('Finished populating!')
	fake = Faker()
	for _ in range(1,50):
		username = fake.first_name()
		password = fake.password()
		bio = fake.text()
		user = User.objects.create_user(username=username, password=password)
		user.save()

		v = Visitor(bio=bio, user=user)
		v.save()

		name_author = fake.name()
		t = Author(name=name_author, user=user)
		t.save()

		article_text = fake.text()
		title_text = fake.text()
		pub_date= fake.date()
		author_article = t
		a = Article(article_text=article_text,title_text=title_text,pub_date=pub_date,
			author_article=author_article)
		a.save()

		comment_text = fake.text()
		pub_date = fake.date()
		visitor_comment = v
		article_comment = a
		c = Comment(comment_text=comment_text, pub_date=pub_date, 
			visitor_comment=visitor_comment, article_comment=article_comment)
		c.save()
