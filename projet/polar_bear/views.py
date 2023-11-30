from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Article

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'polar_bear/list_articles.html', {'articles': articles, 'title': 'Liste des articles'})


def article(request, id):
    article = get_object_or_404(Article, id=id)
    print(article.title)
    print(article.image)
    return render(request, 'polar_bear/article.html', {'article': article})