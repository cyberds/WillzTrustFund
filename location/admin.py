from django.contrib import admin
from .models import State, LocalGovArea

# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)

class LocalGovAreaAdmin(admin.ModelAdmin):
    list_display = ('name','state')


admin.site.register(State, StateAdmin)
admin.site.register(LocalGovArea, LocalGovAreaAdmin)
