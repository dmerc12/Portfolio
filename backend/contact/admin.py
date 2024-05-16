from contact.models import Contact
from django.contrib import admin

# Contact Admin
@admin.register(Contact, site=admin.site)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'subject', 'created', 'read', 'responded']
