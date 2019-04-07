from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('herald/articledetail/<int:article_id>', views.articledetail, name='articledetail'),
    path('herald/authordetail/<int:author_id>', views.authordetail, name='authordetail'),

]