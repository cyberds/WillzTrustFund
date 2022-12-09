from django.contrib import admin
from .models import Lead
# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email','company_name', 'job_title', 'channel', 'involvement', 'program')
    list_per_page = 20

admin.site.register(Lead, LeadAdmin)
