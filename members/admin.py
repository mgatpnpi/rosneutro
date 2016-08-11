from django.contrib import admin
from .models import Person, CustomEmailMessage

class PersonAdmin(admin.ModelAdmin):
    list_display = (
            'first_name',
            'middle_name',
            'last_name',
            'birthday',
            'email',
            'organization',
            'position',
            'degree',
            'interests',
            'publications',
            'approved',
            'confirmed',
            'random_string',
            'published',
            'created',
            'updated',
            )
    search_fields = (
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'organization',
            'position',
            'degree',
            'interests',
            'publications',
            'random_string',
            )
    list_filter = (
            'approved',
            'confirmed',
            'published',
            )

class CustomEmailMessageAdmin(admin.ModelAdmin):
    list_display = (
            'subject',
            'subscribers_only',
            'sent',
            )
    exclude = (
            'sent',
            )

admin.site.register(Person, PersonAdmin)
admin.site.register(CustomEmailMessage, CustomEmailMessageAdmin)
