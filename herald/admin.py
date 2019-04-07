from django.contrib import admin
from .models import Article, Author, Comment, Visitor

# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Visitor)

# admin.site.unregister(User)
# admin.site.register(User)

