from .models import Company, CompanyOverview

def menu_links(request):
    links = Company.objects.get(id=1, is_client=False)
    return dict(company_links=links)

def overview_links(request):
    links = CompanyOverview.objects.get(company_id=1)
    return dict(company_overview_links=links)
