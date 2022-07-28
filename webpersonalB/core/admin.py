from django.contrib import admin
from .models import ContactsDatabase

# Register your models here.

class ContactsDatabaseAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','updated','created', 'email', 'phone')
    search_fields=("name", "created","updated", 'email', 'phone')
    list_filter=('updated',)
    date_hierarchy="updated"

admin.site.register(ContactsDatabase,ContactsDatabaseAdmin)