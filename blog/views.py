from django.shortcuts import render
from blog.models import Article, Author, Paragraph
# Create your views here.

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    paragraphs = Paragraph.objects.filter(article=article)
    articles = Article.objects.all().order_by('-id')[:3]

    dispaly_paragraph = {}
    for paragraph in Paragraph.objects.filter(article=article):
        dispaly_paragraph[article.id] = ' '.join(paragraph.paragraph_content.split(' ')[:18]) + '...'
        break

    context = {
    'article': article,
    'paragraphs': paragraphs,
    'articles': articles,
    'dispaly_paragraph': dispaly_paragraph,
    }

    return render(request, 'article.html', context)

def blog(request, keyword=None):
    if keyword != None:
        article_ids = []
        articles = Article.objects.all()
        for article in articles:
            for paragraph in Paragraph.objects.filter(article=article):
                if keyword in paragraph.paragraph_content:
                    if article.id not in article_ids:
                        article_ids.append(article.id)

        articles = Article.objects.filter(id__in=article_ids).order_by('-id')
        latest_articles = Article.objects.filter().order_by('-id')[:3]
    else:
        articles = Article.objects.filter().order_by('-id')
        latest_articles = articles[:3]

    dispaly_paragraph = {}
    for article in articles:
        for paragraph in Paragraph.objects.filter(article=article):
            dispaly_paragraph[article.id] = ' '.join(paragraph.paragraph_content.split(' ')[:60]) + '...'
            break

    context = {
        'articles': articles,
        'dispaly_paragraph': dispaly_paragraph,
        'latest_articles': latest_articles,
    }

    return render(request, 'blog.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            article_ids = []
            articles = Article.objects.all()
            for article in articles:
                for paragraph in Paragraph.objects.filter(article=article):
                    if keyword in paragraph.paragraph_content:
                        if article.id not in article_ids:
                            article_ids.append(article.id)

            articles = Article.objects.filter(id__in=article_ids).order_by('-id')

    dispaly_paragraph = {}
    for article in articles:
        for paragraph in Paragraph.objects.filter(article=article):
            dispaly_paragraph[article.id] = ' '.join(paragraph.paragraph_content.split(' ')[:60]) + '...'
            break

    latest_articles = Article.objects.filter().order_by('-id')[:3]

    context = {
        'articles': articles,
        'dispaly_paragraph': dispaly_paragraph,
        'latest_articles': latest_articles,
    }

    return render(request, 'blog.html', context)
