# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponse
from .models import Person, CustomEmailMessage
from .tasks import send_email_message
from datetime import datetime
import csv



class PersonAdmin(admin.ModelAdmin):
    list_display = (
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'email',
            'organization',
            'position',
            'degree',
            'interests',
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
            'confirmed',
            'published',
            )
    exclude = [
            'user',
            'random_string',
            'confirmed',
            ]
    actions = [
            'export_to_csv',
            ]
    export_fields = [
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'email',
            'organization',
            'position',
            'degree',
            ]

    def get_table_fields(self):
        opts = self.model._meta
        fields = []
        for field in opts.fields:
            if field.name in self.export_fields:
                fields.append(field)
        return fields

    def export_to_csv(self, request, queryset):
        """
            Generic csv export admin action.
            based on http://djangosnippets.org/snippets/1697/
        """
        fields = self.get_table_fields()
        field_names = [field.name for field in fields]
        field_verbose_names = [field.verbose_name.encode(
                'utf-8'
                ) for field in fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; \
filename=%s.csv' % unicode(self.model._meta).replace('.', '_')

        writer = csv.writer(response)
        writer.writerow(field_verbose_names)
        for obj in queryset:
            writer.writerow([unicode(getattr(obj, field)).encode(
                "utf-8",
                "replace"
                ) for field in field_names])
        return response

    def export_to_csv_all(self, request, queryset):
        return self.export_to_csv(request, Person.objects.all())

    export_to_csv.short_description = u"Скачать CSV файл - помеченых галочками"
    export_to_csv_all.short_description = u"Скачать CSV файл - всех"


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
