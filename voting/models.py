# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField
from pages.models import Translation, Translatable
from members.models import Person
from datetime import datetime

class StartEndModel(models.Model):
    start_date = models.DateTimeField(
            verbose_name = u"Начало",
            null = True
            )
    end_date = models.DateTimeField(
            verbose_name = u"Окончание",
            null = True
            )
    def clean(self):
        if not self.pk:
            if self.end_date <= self.start_date:
                raise ValidationError(u'Перепутаны даты начала и конца голосования')
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
                raise ValidationError(u'Период голосования пересекается')
    class Meta:
        abstract = True

class Voting(Translatable, StartEndModel):
    name = models.CharField(
            max_length = 255,
            verbose_name = u"Внутреннее Название",
            blank = True,
            null = True
            )
    prevoting = models.ForeignKey(
            'PreVoting',
            verbose_name = u"ПреГолосование",
            null = True,
            blank = True
            )
    voters = models.ManyToManyField(
            Person,
            verbose_name = u"Проголосовавшие",
            related_name = "votings",
            blank = True
            )
    def vote_count(self):
        return self.vote_set.count()
    vote_count.short_description = u"число голосов"
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u"Голосование"
        verbose_name_plural = u"Голосования"


class VotingTranslation(Translation):
    class Meta:
        unique_together = ('parent', 'language_code')
        verbose_name = u"Перевод"
        verbose_name_plural = u"Переводы"
    parent = models.ForeignKey(
            'Voting',
            related_name='translations',
            )

    description = RedactorField(
            verbose_name = u"Описание",
            blank = True
            )

class PreVoting(Translatable, StartEndModel):
    prevoters = models.ManyToManyField(
            Person,
            verbose_name = u"Предложившие участников",
            related_name = "prevotings",
            blank = True
            )
    def __unicode__(self):
        return unicode(self.start_date) + u" - " + unicode(self.end_date)
    class Meta:
        verbose_name = u"ПредГолосование"
        verbose_name_plural = u"ПредГолосования"

class PreVotingTranslation(Translation):
    class Meta:
        unique_together = ('parent', 'language_code')
        verbose_name = u"Перевод"
        verbose_name_plural = u"Переводы"
    parent = models.ForeignKey(
            'PreVoting',
            related_name='translations',
            )

    description = RedactorField(
            verbose_name = u"Описание",
            blank = True
            )

class PreVote(models.Model):
    candidates = models.ManyToManyField(
            Person,
            verbose_name = u"Предложенные кандидаты для выборов",
            blank = True
            )
    remarks = models.TextField(
            verbose_name = u"Дополнительные пожелания",
            null=True,
            blank=True
            )
    prevoting = models.ForeignKey(
            PreVoting,
            verbose_name = u"Предварительное голосование",
            )
    class Meta:
        verbose_name = u"Предварительный голос"
        verbose_name_plural = u"Предварительные голоса"

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
    agree = models.BooleanField(
            verbose_name = u"Подтвердил согласие",
            default = False
            )
    def vote_count(self):
        return self.vote_set.count()
    vote_count.short_description = u"число голосов"
    def __unicode__(self):
        return self.person.first_name + u" " + self.person.last_name + u" " + self.person.middle_name
    class Meta:
        verbose_name = u"Кандидат"
        verbose_name_plural = u"Кандидаты"
        unique_together = ['person', 'voting']

class CandidateTranslation(Translation):
    class Meta:
        unique_together = ('parent', 'language_code')
        verbose_name = u"Перевод"
        verbose_name_plural = u"Переводы"
    parent = models.ForeignKey(
            'Candidate',
            related_name='translations',
            )

    description = RedactorField(u"Описание")

class Vote(models.Model):
    voting = models.ForeignKey(
            Voting
            )
    candidate = models.ForeignKey(
            Candidate
            )
