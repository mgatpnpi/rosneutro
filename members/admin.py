# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Person, CustomEmailMessage
from .tasks import send_email_message
from datetime import datetime

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
            )
    list_filter = (
            'approved',
            'confirmed',
            'published',
            )
    exclude = [
            'user',
            'random_string',
            'confirmed',
            ]

class CustomEmailMessageAdmin(admin.ModelAdmin):
    list_display = (
            'subject',
            'subscribers_only',
            'sent',
            )
    exclude = (
            'sent',
            )
    actions = ['send_checked']
    def send_checked(self, request, queryset):
        for message in queryset:
            if not message.sent:
                attach1 = None
                attach2 = None
                attach3 = None
                if message.attachment1:
                    attach1 = message.attachment1.path
                if message.attachment2:
                    attach2 = message.attachment2.path
                if message.attachment3:
                    attach3 = message.attachment3.path

                if message.subscribers_only:
                    for person in Person.objects.filter(
                            subscribed = True
                            ):
                        send_email_message.delay(
                                message.subject,
                                message.message,
                                person.email,
                                attach1,
                                attach2,
                                attach3
                                )
                else:
                    for person in Person.objects.filter(
                            confirmed = True
                            ):
                        send_email_message.delay(
                                message.subject,
                                message.message,
                                person.email,
                                attach1,
                                attach2,
                                attach3
                                )
                message.sent = datetime.now()
                message.save()
    send_checked.short_description = u"Запустить выбранные рассылки"
            

admin.site.register(Person, PersonAdmin)
admin.site.register(CustomEmailMessage, CustomEmailMessageAdmin)
