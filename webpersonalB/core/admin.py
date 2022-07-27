from django.contrib import admin
from .forms import ContactForm

# Register your models here.

#class ContactFormAdmin(admin.ModelAdmin):
    #list_display=('name','msj',)
    #search_fields=("name","email","phone","msj")
    #list_filter=("email")
    #date_hierarchy=("phone")
    #pass

#admin.site.register(ContactForm, ContactFormAdmin)