# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from voting.models import PreVoting, Voting
from members.forms import PersonForm
from .models import CustomSettings
from datetime import datetime

class PageContextMixin(ContextMixin):
    keywords = ''
    description = ''
    module = False
    voting = None
    prevoting = None
    def getcurrentstartendmodel(self, model):
        now = datetime.now()
        return model.objects.filter(
                    start_date__lt = now,
                    end_date__gt = now
                    ).first()
    def getvoting(self):
        if self.voting == None:
            self.voting = self.getcurrentstartendmodel(Voting)
            if not self.voting:
                self.voting = False
    def getprevoting(self):
        if self.prevoting == None:
            self.prevoting = self.getcurrentstartendmodel(PreVoting)
            if not self.prevoting:
                self.prevoting = False
    def get_context_data(self, **kwargs):
        context = super(PageContextMixin, self).get_context_data(**kwargs)
        custom_settings = CustomSettings.objects.first()
        context["custom_settings"] = custom_settings
        context["path"] = self.request.path
        context['keywords'] = self.keywords
        context['description'] = self.description
        if self.module:
            context["module"] = self.module
        self.getvoting()
        self.getprevoting()
        context['voting'] = self.voting
        context['prevoting'] = self.prevoting
        return context

class NoPageView(PageContextMixin, TemplateView):
    template_name = '404.html'

class MainPageView(PageContextMixin, TemplateView):
    module = 'main'
    template_name = 'main.html'
    keywords = 'Russian Neutron Scattering Society, Российское Нейтронографическое Общество, ECNS, ENSA, РНИКС, РНСИКС'
    description = 'В состав российского нейтронографического общества входит более 300 ведущих научных специалистов, использующих в своей деятельности методы нейтронного рассеяния.'
    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['form'] = PersonForm
        return context

class MessageView(PageContextMixin, TemplateView):
    template_name = 'message.html'
