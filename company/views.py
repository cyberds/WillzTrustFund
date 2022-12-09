from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, CompanyOverview
from staff.models import Staff
from program.models import Program, Project, Activity, ActivityImage
# from staff.models import Staff


def company(request):
    company = Company.objects.get(id=1, is_client=False)
    company_overview = CompanyOverview.objects.get(company=company)
    programs = Program.objects.filter(company=company)[:3]
    activities = Activity.objects.filter(company=company)[:3]
    staff = Staff.objects.filter(company=company, is_active=True)[:6]

    context = {
        'company': company,
        'company_overview': company_overview,
        'programs': programs,
        'activities': activities,
        'staff': staff,
    }
    return render(request, 'about.html', context)
