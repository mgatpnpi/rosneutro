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
    class Meta:
        model = PreVote
        fields = ['remarks', 'candidates']
