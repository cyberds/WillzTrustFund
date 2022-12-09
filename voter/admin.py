from django.contrib import admin
from .models import Voter

# Register your models here.
class VoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_registered', 'willing_to_register', 'created_date', 'modified_date')
    list_filter = ['created_date', 'is_registered']
    list_per_page = 50

admin.site.register(Voter, VoterAdmin)
