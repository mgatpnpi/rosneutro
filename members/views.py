# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import \
        TemplateView, \
        DetailView, \
        ListView, \
        CreateView, \
        UpdateView, \
        FormView
from django.views.defaults import permission_denied
from django.forms.models import model_to_dict
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
from .forms import \
        PersonForm, \
        RequestLinkForm, \
        MemberEditProfileForm
from .tasks import \
        confirmation_link_email, \
        secret_link_email


class MemberOnlyMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.person:
            return permission_denied(request)
        self.person = request.user.person
        return super(MemberOnlyMixin, self).dispatch(request, *args, **kwargs)


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
            try:
                self.secret = queryset.get(secret = self.kwargs['secret'])
            except Secret.DoesNotExist:
                return permission_denied(request)
            self.secret.used = True
            self.secret.save()
            try:
                user = authenticate(
                        username = self.secret.user.username,
                        password = self.secret.secret
                        )
                login(request, user)
            except:
                return permission_denied(request)

        return super(MemberEnterView, self).dispatch(request, *args, **kwargs)

class MemberLogoutView(PageContextMixin, TemplateView):
    template_name = "member_logout.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            random_password = generate_random_string()
            request.user.set_password(random_password)
            request.user.save()
            logout(request)
        return super(MemberLogoutView, self).dispatch(request, *args, **kwargs)

class MemberEditProfileView(PageContextMixin, MemberOnlyMixin, UpdateView):
    template_name = "member_edit_profile.html"
    model = Person
    form_class = MemberEditProfileForm
    def get_success_url(self):
        return reverse("member_edit_profile_success")
    def get_object(self):
        return self.request.user.person

class MemberEditProfileSuccessView(PageContextMixin, MemberOnlyMixin, DetailView):
    template_name = "member_edit_profile_success.html"
    model = Person
    def get_object(self):
        obj = self.request.user.person
        obj.fields =[ 
                (
                    obj._meta.get_field(name).verbose_name,
                    obj._meta.get_field(name).value_to_string(obj)
                    )
                    for name in obj.MEMBER_EDIT_FIELDS
                    if getattr(obj, name)
                 ]
        return obj
