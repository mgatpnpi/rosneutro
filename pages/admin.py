from django.contrib import admin

from django.contrib import admin
from django.conf import settings
from .models import CustomSettings, CustomSettingsTranslation

class TranslationInlineMixin(object):
    extra = len(settings.LANGUAGES)
    max_num = len(settings.LANGUAGES)

class CustomSettingsTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = CustomSettingsTranslation

class CustomSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = [ CustomSettingsTranslationInline ]

admin.site.register(CustomSettings, CustomSettingsAdmin)
