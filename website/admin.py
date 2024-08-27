from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_date', 'updated_date')

admin.site.register(Contact, ContactAdmin)
