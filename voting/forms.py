# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __
from members.forms import ModelBootstrappedForm
from members.models import Person
from .models import PreVote, Vote

class VoteForm(ModelBootstrappedForm):
    class Meta:
        model = Vote
        fields = ['candidate',]
        widgets = {
                'candidate': forms.RadioSelect()
                }

class PreVoteForm(ModelBootstrappedForm):
    def clean_candidates(self):
        candidates = self.cleaned_data['candidates']
        if len(candidates) > 3:
            raise forms.ValidationError(__(u"Можно предложить не более трех человек"))
        return candidates
    class Meta:
        model = PreVote
        fields = [
                'candidates',
                'remarks',
                ]
