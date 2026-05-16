from django.contrib import admin
from web.models import contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ['name', 'message']
admin.site.register(contact, ContactAdmin)

# Register your models here.
