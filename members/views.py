# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import \
        TemplateView, \
        DetailView, \
        ListView, \
        CreateView, \
        FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from pages.views import PageContextMixin
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
from .models import Person, Secret, generate_random_string
from .forms import PersonForm, RequestLinkForm
from .tasks import \
        confirmation_link_email, \
        secret_link_email

class RegistrationView(PageContextMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = "registration.html"
    def get_success_url(self):
        confirmation_link_email.delay(
                self.object.email,
                self.object.random_string
                )
        return reverse('members_success')

class RegistrationSuccessView(PageContextMixin, TemplateView):
    template_name = "registration_success.html"
    
class ConfirmEmailView(PageContextMixin, TemplateView):
    template_name = "confirm_email.html"
    def dispatch(self, request, *args, **kwargs):
        queryset = Person.objects.filter(
                published = True,
                created__gt = date.today() - relativedelta(months = 1)
                )
        person = get_object_or_404(
                queryset,
                random_string = self.kwargs['random_string']
                )
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

class MemberRequestSessionView(PageContextMixin, FormView):
    form_class = RequestLinkForm
    template_name = "member_request_session.html"
    def get_success_url(self):
        return reverse("member_request_session_success")
    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            form.add_error('email', _(u"Такого E-mail нет у зарегистрированых участников"))
            return self.form_invalid(form)
 
        if Secret.objects.filter(
                user=user,
                created__gt = datetime.now() -
                    relativedelta(hours = Secret.TIME_TO_LIVE),
                used = False
                        ):
            form.add_error('email', _(u"На ваш E-mail уже выслана ссылка для входа и она еще действует"))
            return self.form_invalid(form)

        secret = Secret.objects.create(
                user = user
                )
        secret_link_email.delay(email, secret.secret)

        return super(MemberRequestSessionView, self).form_valid(form)

class MemberRequestSessioniSuccessView(PageContextMixin, TemplateView):
    template_name = "member_request_session_success.html"

class MemberEnterView(PageContextMixin, TemplateView):
    template_name = "member_enter.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            queryset = Secret.objects.filter(
                    created__gt = datetime.now() -
                        relativedelta(hours = Secret.TIME_TO_LIVE),
                    used = False
                    )
            self.secret = get_object_or_404(
                    queryset,
                    secret = self.kwargs['secret']
                    )
            self.secret.used = True
            self.secret.save()
            user = authenticate(
                    username = self.secret.user.username,
                    password = self.secret.secret
                    )
            login(request, user)
        return super(MemberEnterView, self).dispatch(request, *args, **kwargs)

class MemberLogoutView(PageContextMixin, TemplateView):
    template_name = "member_logout.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            random_password = generate_random_string()
            request.user.set_password(random_password)
            request.user.save()
            for secret in request.user.secret_set.filter(
                    created__gt = datetime.now() -
                        relativedelta(hours = Secret.TIME_TO_LIVE),
                    used = False
                    ):
                secret.used = True
                secret.save()

            logout(request)
        return super(MemberLogoutView, self).dispatch(request, *args, **kwargs)
