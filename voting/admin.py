# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PreVote, PreVoting, PreVotingTranslation, Voting, VotingTranslation, Candidate, CandidateTranslation
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
    extra = 0
    model = Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('person', 'voting', 'agree', 'vote_count')
    list_editable = ('agree',)
    list_filter = ['voting',]
    inlines = [CandidateTranslationInline,]

class VotingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'vote_count')
    inlines = [VotingTranslationInline, CandidateInline]
    exclude = ['voters',]

class VotingInline(admin.StackedInline):
    extra = 1
    max_num = 1
    model = Voting
    exclude = ['voters']

class PreVotingTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = PreVotingTranslation

class PreVotingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'start_date', 'end_date')
    inlines = [VotingInline, PreVotingTranslationInline]
    exclude = ['prevoters',]

class PreVoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'show_candidates', 'remarks')
    actions = ['move_to_candidates',]
    list_filter = ['prevoting',]
    def move_to_candidates(self,request, queryset):
        candidates_pks = []
        votings_pks = []
        for prevote in queryset:
            candidates_pks += prevote.candidates.values_list('pk', flat=True)
            votings_pks += prevote.prevoting.voting_set.values_list(
                    'pk',
                    flat=True
                    )
        for voting_pk in set(votings_pks):
            voting = Voting.objects.get(pk=voting_pk)
            for person_pk in set(candidates_pks):
                person = Person.objects.get(pk=person_pk)
                Candidate.objects.create(
                        voting = voting,
                        person = person
                        )
    move_to_candidates.short_description = u"Создать кандидатов (вкладка Кандидаты)"

admin.site.register(Voting, VotingAdmin)
admin.site.register(PreVoting, PreVotingAdmin)
admin.site.register(PreVote, PreVoteAdmin)
admin.site.register(Candidate, CandidateAdmin)
