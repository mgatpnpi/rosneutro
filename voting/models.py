# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from redactor.fields import RedactorField
from pages.models import Translation, Translatable
from members.models import Person
from datetime import datetime

class Voting(Translatable):
    name = models.CharField(
            max_length = 255,
            verbose_name = u"Внутреннее Название",
            blank = True,
            null = True
            )
    start_date = models.DateTimeField(
            verbose_name = u"Начало голосования",
            null = True
            )
    end_date = models.DateTimeField(
            verbose_name = u"Окончание голосования",
            null = True
            )
    def vote_count(self):
        return self.vote_set.count()
    vote_count.short_description = "число голосов"
    def __unicode__(self):
        return self.name
    def clean(self):
        if not self.pk:
            if self.end_date <= self.start_date:
                raise ValidationError('Перепутаны даты начала и конца голосования')
            if Voting.objects.filter(
                        start_date__lt = self.start_date,
                        end_date__gt = self.start_date
                    ) or Voting.objects.filter(
                        start_date__lt = self.end_date,
                        end_date__gt = self.end_date
                    ) or Voting.objects.filter(
                            start_date__gt = self.start_date,
                            end_date__lt = self.end_date
                            ):
                raise ValidationError('Период голосования пересекается')
    class Meta:
        verbose_name = u"Голосование"
        verbose_name_plural = u"Голосования"


class VotingTranslation(Translation):
    class Meta:
        unique_together = ('parent', 'language_code')
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"
    parent = models.ForeignKey(
            'Voting',
            related_name='translations',
            )

    description = RedactorField(
            verbose_name = u"Описание",
            blank = True
            )

class Candidate(Translatable):
    voting = models.ForeignKey(
            Voting,
            verbose_name = u"Голосование, в котором участвует"
            )
    person = models.ForeignKey(
            Person,
            verbose_name = u"Человек из участников",
            limit_choices_to={'confirmed': True, 'published': True}
            )
    def vote_count(self):
        return self.vote_set.count()
    vote_count.short_description = "число голосов"
    def __unicode__(self):
        return self.person.first_name + " " + self.person.last_name
    class Meta:
        verbose_name = u"Кандидат"
        verbose_name_plural = u"Кандидаты"

class CandidateTranslation(Translation):
    class Meta:
        unique_together = ('parent', 'language_code')
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"
    parent = models.ForeignKey(
            'Candidate',
            related_name='translations',
            )

    description = RedactorField("Описание")

class Vote(models.Model):
    person = models.ForeignKey(
            Person
            )
    voting = models.ForeignKey(
            Voting
            )
    candidate = models.ForeignKey(
            Candidate
            )
    class Meta:
        unique_together = ['person', 'voting']

