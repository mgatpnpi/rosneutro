from django.shortcuts import render
from django.views.generic import  TemplateView, DetailView, ListView,  CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from pages.views import PageContextMixin
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime
from .models import Person
from .forms import PersonForm
from .tasks import secret_link_email

class RegistrationView(PageContextMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = "registration.html"
    def get_success_url(self):
        secret_link_email.delay(self.object)
        return reverse('members_success')

class RegistrationSuccessView(PageContextMixin, TemplateView):
    template_name = "registration_success.html"
    
class ConfirmEmailView(PageContextMixin, TemplateView):
    template_name = "confirm_email.html"
    def dispatch(self, request, *args, **kwargs):
        queryset = Person.objects.filter(published = True, created__gt = date.today() - relativedelta(months = 1))
        person = get_object_or_404(queryset, random_string = self.kwargs['random_string'])
        person.confirmed = True
        person.subscribed = True
        person.save()
        return super(ConfirmEmailView, self).dispatch(request, *args, **kwargs)

class MembersListView(PageContextMixin, ListView):
    context_object_name = "members"
    model = Person
    template_name = "members_list.html"
    def get_queryset(self):
        return Person.objects.filter(confirmed = True, published = True)
