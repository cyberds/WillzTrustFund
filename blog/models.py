from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_url = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/authors')
    created_date = models.DateTimeField(blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name

class Article(models.Model):
    article_title = models.CharField(max_length=50)
    article_subtitle = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/article')
    article_author = models.ManyToManyField(Author)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(blank=True, null=True)
    tags = models.TextField(max_length=200, blank=True, null=True)

    def get_url(self):
        return reverse('article', args=[self.id])

    def __str__(self):
        return self.article_title

class Paragraph(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    paragraph_title = models.CharField(max_length=50)
    paragraph_content = models.TextField(max_length=2500)
    paragraph_image = models.ImageField(upload_to='photos/paragraph', blank=True, null=True)

    def __str__(self):
        return self.paragraph_title
