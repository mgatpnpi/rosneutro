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
    extra = 3
    model = Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('person', 'voting', 'agree', 'vote_count')
    list_editable = ('agree',)
    inlines = [CandidateTranslationInline,]

class VotingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'vote_count')
    inlines = [VotingTranslationInline, CandidateInline]

class VotingInline(admin.StackedInline):
    extra = 1
    max_num = 1
    model = Voting

class PreVotingTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = PreVotingTranslation

class PreVotingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'start_date', 'end_date')
    inlines = [VotingInline, PreVotingTranslationInline]

class PreVoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'show_candidates', 'remarks')
    actions = ['move_to_candidates',]
    def move_to_candidates(self,request, queryset):
        for prevote in queryset:
            for person in prevote.candidates.all():
                for voting in prevote.prevoting.voting_set.all():
                    Candidate.objects.create(
                            voting = voting,
                            person = person
                            )
    move_to_candidates.short_description = u"Создать кандидатов (вкладка Кандидаты)"

admin.site.register(Voting, VotingAdmin)
admin.site.register(PreVoting, PreVotingAdmin)
admin.site.register(PreVote, PreVoteAdmin)
admin.site.register(Candidate, CandidateAdmin)
