from random import randint
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fnews.settings')

import django
django.setup()

from herald.models import Article, User, Author, Comment
from faker import Faker


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
		name_author = fake.name()
		t = Author(name=name_author)
		t.save()

		name_user = fake.name()
		u = User(name=name_user)
		u.save()

		article_text = fake.text()
		title_text = fake.text()
		pub_date= fake.date()
		# author_article = t
		a = Article(article_text=article_text,title_text=title_text,pub_date=pub_date,author_article=t)
		a.save()

		comment_text = fake.text()
		# user_comment = u
		# article_comment = a
		c = Comment(comment_text=comment_text, user_comment=u, article_comment = a)
		c.save()
	