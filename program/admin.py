from django.contrib import admin
from .models import Program, Project, Activity, ActivityImage

# Register your models here.
class ActivityImageAdmin(admin.ModelAdmin):
    list_display = ('image_name','activity', 'project')
    list_per_page = 20

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'activity_date','project', 'program')
    list_filter = ['created_date']
    list_per_page = 20

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('project_name',)}
    list_display = ('project_name', 'program')
    list_filter = ['created_date']
    list_per_page = 20

class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('program_name',)}
    list_display = ('program_name', 'company')
    list_filter = ['created_date']
    list_per_page = 20

admin.site.register(ActivityImage, ActivityImageAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Program, ProgramAdmin)
