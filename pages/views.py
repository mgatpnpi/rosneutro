from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from .models import CustomSettings
from members.forms import PersonForm

class PageContextMixin(ContextMixin):
    module = False
    def get_context_data(self, **kwargs):
        context = super(PageContextMixin, self).get_context_data(**kwargs)
        custom_settings = CustomSettings.objects.first()
        context["custom_settings"] = custom_settings
        context["path"] = self.request.path
        if self.module:
            context["module"] = self.module
        return context

class MainPageView(PageContextMixin, TemplateView):
    module = 'main'
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['form'] = PersonForm
        return context
