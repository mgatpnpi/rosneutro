# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import \
        TemplateView, \
        FormView
from django.http import Http404
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy, reverse
from pages.views import PageContextMixin
from members.views import MemberOnlyMixin
from .models import Vote, Voting, Candidate
from .forms import VoteForm

class NoVotesAtTheMomentView(PageContextMixin, MemberOnlyMixin, TemplateView):
    template_name = 'no_votes_at_the_moment.html'

class VotesSuccessView(PageContextMixin, MemberOnlyMixin, TemplateView):
    template_name = 'votes_success.html'

class VotesView(PageContextMixin, MemberOnlyMixin, FormView):
    form_class = VoteForm
    template_name = "voting.html" 
    success_url = reverse_lazy('votes_success')
    def form_valid(self, form):
        candidate = form.cleaned_data['candidate']
        if not candidate:
            form.add_error('candidate', _("Обязательно нужно выбрать одного из представленных кандидатов"))
            return self.form_invalid(form)
        Vote.objects.create(
                voting = self.voting,
                person = self.person,
                candidate = candidate
                )
        return super(VotesView, self).form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        self.getvoting()
        if not self.voting:
            return NoVotesAtTheMomentView.as_view()(request, *args, **kwargs)
        if request.user.is_authenticated() and hasattr(request.user, 'person') and request.user.person.vote_set.filter(voting = self.voting):
            return VotesSuccessView.as_view()(request, *args, **kwargs)
        return super(VotesView, self).dispatch(request, *args, **kwargs)
