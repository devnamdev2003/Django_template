from django.contrib import admin
from home.models import ContactInfo
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'number', 'mess')
    list_filter = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email', 'number', 'mess')


admin.site.register(ContactInfo, ContactAdmin)
