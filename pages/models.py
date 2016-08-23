# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from django.utils.translation import get_language
from django.conf import settings

class Translation(models.Model):
    language_code = models.CharField("Язык", max_length = 7, choices = settings.LANGUAGES)
    class Meta:
        abstract = True
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"

class Translatable(models.Model):
    translated = False
    def translate(self):
        try:
            translation = self.translations.get(language_code = get_language())
        except Exception:
            if self.translations:  
                translation = self.translations.first()
            else:
                return False
        self.translated = translation
        return True
    def __init__(self, *args, **kwargs):
        super(Translatable, self).__init__(*args, **kwargs)
        self.translate()
    class Meta:
        abstract = True

class CustomSettings(Translatable):
    class Meta:
        verbose_name = "Настройки"


class CustomSettingsTranslation(Translation):
    class Meta:
        unique_together = ( 'parent', 'language_code')
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"
    parent = models.ForeignKey(
            'CustomSettings',
            related_name='translations'
            )

    mainpagecontent = RedactorField(
            verbose_name = "Содержимое главной страницы"
            )
    formpagecontent = RedactorField(
            verbose_name = "Содержимое страницы с формой регистрации",
            null = True,
            blank = True
            )
    lettercontent = RedactorField(
            "Обращение Вахрушева",
            null = True,
            blank = True
            )
    requestsessioncontent = RedactorField(
            "Содержимое страницы с формой запроса ссылки для входа",
            null = True,
            blank = True
            )
