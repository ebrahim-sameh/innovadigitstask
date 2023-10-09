from django.contrib import admin
from .models import Contact, PhoneNumber

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber

class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline]

admin.site.register(Contact, ContactAdmin)
admin.site.register(PhoneNumber)
