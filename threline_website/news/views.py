from django.shortcuts import render
from .models import NewsArticle


def news_home_view(request):
    news_article = NewsArticle
    context = {'news_article': news_article}
    return render(request, 'index.html', context)
