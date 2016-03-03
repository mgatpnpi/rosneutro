from django.shortcuts import render
from django.views.generic import  TemplateView, DetailView, ListView,  CreateView
from pages.views import PageContextMixin
from .models import Person

class MembersListView(PageContextMixin, ListView):
    context_object_name = "persons"
    model = Person
    template_name = "members_list.html"

class RegistrationView(PageContextMixin, CreateView):
    model = Person
    template_name = "registration.html"
    
class ConfirmEmailView(PageContextMixin, TemplateView):
    template_name = "confirm_email.html"
    def dispatch(self, request, *args, **kwargs):
        queryset = Person.objects.filter(published = True, created__gt = date.today - timedelta(month = 1))
        person = get_object_or_404(queryset, random_string = self.kwargs['random_string'])
        person.confirmed = True
        person.save()
        return super(ConfirmEmailView, self).dispatch(request, *args, **kwargs)

        
