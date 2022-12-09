from django.contrib import admin
from .models import Author, Article, Paragraph

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'job_title', 'email', 'company_name', 'created_date')
    list_filter = ['created_date']
    list_per_page = 20

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'is_active', 'created_date')
    list_filter = ['is_active', 'created_date']
    list_per_page = 20

class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('article', 'paragraph_title')
    list_per_page = 20

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
