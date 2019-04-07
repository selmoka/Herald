from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse, Http404
from .models import Article, Author, Visitor, Comment
from datetime import datetime

# Create your views here.
def index(request):
	# vehicles = Vehicle.objects.all()
	return render(request, 'articles.html',{
		'articles': Article.objects.all().order_by('-pub_date')
	}) 

def articledetail(request, article_id):
	article = Article.objects.get(pk=article_id)

	if request.method == 'POST':
		comment_text = request.POST['comment']
		pub_date = datetime.now()
		visitor_comment = Visitor.objects.get(user=request.user)
		article_comment = article
		c = Comment(comment_text=comment_text,pub_date=pub_date,
			visitor_comment=visitor_comment, article_comment=article_comment)
		c.save()

	if request.user.is_authenticated:
		comments = article.comment_set.all()
		print('you are authed as: '.format(request.user.username))
		return render(request, 'articledetailwithcomment.html',
			{
			'article': article,
			'user': request.user,
			'comments': comments
			})
	else:
		return render(request, 'articledetail.html',{'article': article})
	
def authordetail(request, author_id):
# 	q = Question.objects.get(pk=1)
	# q.choice_set.all()
	a = Author.objects.get(pk=author_id)
	authorname = a.name
	articles = a.article_set.all()
	return render(request, 'authordetail.html', {'articles' : articles, 'authorname': authorname})

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		bio = request.POST['bio']
		user = User.objects.create_user(username=username, password=password)
		if user is not None:
			user.save()
			visitor = Visitor(bio=bio, user=user)
			visitor.save()
			login(request, user)
	return render(request, 'signup.html')