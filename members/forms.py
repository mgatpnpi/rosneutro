# -*- coding: utf-8 -*-
from django import forms
from .models import Person
from captcha.fields import ReCaptchaField
from datetime import date

class ModelBootstrappedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelBootstrappedForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if not field_name == 'captcha':
                field = self.fields.get(field_name)
                if field:
                    field.widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                    })
                if type(field.widget) in (forms.DateInput,):
                    field.widget.attrs.update({
                        'class': 'form-control datepicker',
                        })
                    field.widget.input_type = 'date'
        #self.fields.values()[0].widget.attrs['autofocus'] = 'autofocus'

class PersonForm(ModelBootstrappedForm):
    captcha = ReCaptchaField(use_ssl=True, attrs={'theme':'clean', 'lang': 'ru'})
    class Meta:
        model = Person
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'email',
            'organization',
            'position',
            'degree',
            'interests',
            'publications',
        ]
    
