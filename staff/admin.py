from django.contrib import admin
from .models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'job_title', 'employment_date', 'terminate_date', 'is_management', 'is_primary_contact')

admin.site.register(Staff, StaffAdmin)
