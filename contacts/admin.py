from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'contact_date')
    list_display_links = ('name', 'contact_date')
    search_fields = ('name', 'contact_date')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
