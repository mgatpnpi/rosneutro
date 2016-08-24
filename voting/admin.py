# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Voting, VotingTranslation, Candidate, CandidateTranslation
from members.models import Person
from pages.admin import TranslationInlineMixin

class PersonFieldSortMixin(object):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field == 'person':
            kwargs['queryset'] = Person.objects.order_by('last_name')
        return super(PersonFieldSortMixin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class VotingTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = VotingTranslation

class CandidateTranslationInline(TranslationInlineMixin, PersonFieldSortMixin,  admin.StackedInline):
    model = CandidateTranslation

class CandidateInline(PersonFieldSortMixin, admin.StackedInline):
    extra = 3
    model = Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('person', 'voting')
    inlines = [CandidateTranslationInline,]

class VotingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    inlines = [VotingTranslationInline, CandidateInline]

admin.site.register(Voting, VotingAdmin)
admin.site.register(Candidate, CandidateAdmin)
