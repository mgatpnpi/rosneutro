# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import get_language
from .models import Person
from captcha.fields import ReCaptchaField
from datetime import date

def translate_captcha(form):
    try:
        form.fields.get('captcha').widget.js_attrs = {'lang': get_language()[:2]}
    except Exception:
        pass

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
        translate_captcha(self)
        #self.fields.values()[0].widget.attrs['autofocus'] = 'autofocus'

class PersonForm(ModelBootstrappedForm):
    captcha = ReCaptchaField(use_ssl=True, attrs={'theme':'clean'})
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
            'interests',
            'degree',
            'note'
        ]

class RequestLinkForm(ModelBootstrappedForm):
    class Meta:
        model = Person
        fields = [
                'email',
                ]

class MemberEditProfileForm(ModelBootstrappedForm):
    class Meta:
        model = Person
        fields = Person.MEMBER_EDIT_FIELDS
