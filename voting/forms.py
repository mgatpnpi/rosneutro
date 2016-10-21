# -*- coding: utf-8 -*-
from django import forms
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
    candidates = forms.ModelMultipleChoiceField(
            queryset = Person.objects.filter(
                confirmed = True,
                published = True
                ).order_by('last_name'),
            widget = forms.CheckboxSelectMultiple
            )
    class Meta:
        model = PreVote
        fields = ['remarks', ]
