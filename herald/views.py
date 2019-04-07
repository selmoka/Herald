from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article, Author

# Create your views here.
def index(request):
	# vehicles = Vehicle.objects.all()
	return render(request, 'articles.html',{
		'articles': Article.objects.all().order_by('-pub_date')
	}) 

def articledetail(request, article_id):
	# vehicles = Vehicle.objects.all()
	article = Article.objects.get(pk=article_id)
	return render(request, 'articledetail.html',{'article': article})
	
def authordetail(request, author_id):

# 	q = Question.objects.get(pk=1)
	# q.choice_set.all()
	a = Author.objects.get(pk=author_id)
	authorname = a.name
	articles = a.article_set.all()
	return render(request, 'authordetail.html', {'articles' : articles, 'authorname': authorname})