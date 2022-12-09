from django.contrib import admin
from .models import Company, CompanyOverview

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'created_date', 'state', 'modified_date', 'is_client')
    list_editable = ('is_client',)
    list_filter = ('company_name', 'state', 'modified_date')

class CompanyOverviewAdmin(admin.ModelAdmin):
    list_display = ('company',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyOverview, CompanyOverviewAdmin)
