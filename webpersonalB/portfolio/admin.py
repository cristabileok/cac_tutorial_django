from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','updated','created')
    search_fields=("title","created","updated")
    list_filter=('updated',)
    date_hierarchy="updated"

admin.site.register(Project, ProjectAdmin)