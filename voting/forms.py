# -*- coding: utf-8 -*-
from django import forms
from members.forms import ModelBootstrappedForm
from .models import Vote

class VoteForm(ModelBootstrappedForm):
    class Meta:
        model = Vote
        fields = ['candidate',]
        widgets = {
                'candidate': forms.RadioSelect()
                }
