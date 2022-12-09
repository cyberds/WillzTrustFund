from .models import Program, Activity, ActivityImage
from company.models import Company

def menu_links(request):
    company = Company.objects.get(id=1, is_client=False)
    links =  Program.objects.filter(company=company)
    return dict(program_links=links)

def image_menu_links(request):
    company = Company.objects.get(id=1, is_client=False)
    program =  Program.objects.filter(company=company)
    links = ActivityImage.objects.filter(program_id__in=program)[:6]
    return dict(image_links=links)


def activity_menu_links(request):
    company = Company.objects.get(id=1, is_client=False)
    program =  Program.objects.filter(company=company)
    links = Activity.objects.filter(program_id__in=program).order_by('-id')[:6]
    return dict(activity_links=links)
