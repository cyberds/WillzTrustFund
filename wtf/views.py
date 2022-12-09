from django.shortcuts import render
from company.models import Company, CompanyOverview
from program.models import Program, Project, Activity, ActivityImage
from staff.models import Staff
# from project.models import Project, ProjectImages
from blog.models import Article, Author, Paragraph

def home(request):
    company = Company.objects.get(id=1, is_client=False)
    company_overview = CompanyOverview.objects.get(company=company)
    programs = Program.objects.filter(company=company)[:3]
    activities = Activity.objects.filter(company=company).order_by('-id')[:3]

    program_desc = {}
    for program in programs:
        program_desc[program.id] = ' '.join(program.program_description.split(' ')[:50]) + '...'

    articles = Article.objects.all().order_by('-id')[:3]
    dispaly_paragraph = {}
    for article in articles:
        for paragraph in Paragraph.objects.filter(article=article):
            dispaly_paragraph[article.id] = ' '.join(paragraph.paragraph_content.split(' ')[:18]) + '...'
            break

    context = {
        'company': company,
        'company_overview': company_overview,
        'programs': programs,
        'program_desc': program_desc,
        'activities': activities,
        # 'display_images': display_images,
        'articles': articles,
        'dispaly_paragraph': dispaly_paragraph,
    }

    return render(request, 'home.html', context)
