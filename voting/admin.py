from django.contrib import admin
from .models import Voting, VotingTranslation, Candidate, CandidateTranslation
from pages.admin import TranslationInlineMixin

class VotingTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = VotingTranslation

class CandidateTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = CandidateTranslation

class CandidateInline(admin.StackedInline):
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
