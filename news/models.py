# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from django.utils.encoding import smart_text
from pages.models import Translation, Translatable

class NewsPost(Translatable):
    published = models.BooleanField(
            default = True
            )
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        if self.translated:
            return smart_text(self.translated.title)
        return ""
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ('-created',)

class NewsPostTranslation(Translation):
    parent = models.ForeignKey(NewsPost, related_name = 'translations')

    title = models.CharField(
            verbose_name = u"Заголовок",
            max_length = 250
            )
    content = RedactorField(
            verbose_name = u"Основной текст - полное содержание новости",
            blank = True,
            null = True
            )
    def __unicode__(self):
        return u"Новость"

