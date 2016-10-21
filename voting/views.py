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
from .forms import PreVoteForm, VoteForm

class NoVotesAtTheMomentView(PageContextMixin, MemberOnlyMixin, TemplateView):
    template_name = 'no_votes_at_the_moment.html'

class PreVotesSuccessView(MemberOnlyMixin, PageContextMixin, TemplateView):
    template_name = 'prevotes_success.html'

class PreVotesView(PageContextMixin, MemberOnlyMixin, FormView):
    form_class = PreVoteForm
    template_name = "prevoting.html"
    success_url = reverse_lazy("prevotes")
    def form_valid(self, form):
        self.prevoting.proposed_candidates.add(form.cleaned_data['candidates'])
        self.prevoting.prevoters.add(self.person)
        self.prevoting.save()
        
        return super(PreVotesView, self).form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        self.getprevoting()
        if not self.prevoting:
            return NoVotesAtTheMomentView.as_view()(request, *args, **kwargs)
        if hasattr(request.user, 'person') \
                and request.user.person.pk in list(
                        self.prevoting.prevoters.all().values_list('pk', flat = True)
                        ):
            return PreVotesSuccessView.as_view()(request, *args, **kwargs)
        return super(PreVotesView, self).dispatch(request, *args, **kwargs)

class VotesSuccessView(PageContextMixin, MemberOnlyMixin, TemplateView):
    template_name = 'votes_success.html'

class VotesView(MemberOnlyMixin, PageContextMixin, FormView):
    form_class = VoteForm
    template_name = "voting.html" 
    success_url = reverse_lazy('votes')
    def form_valid(self, form):
        candidate = form.cleaned_data['candidate']
        if not candidate:
            form.add_error('candidate', _("Обязательно нужно выбрать одного из представленных кандидатов"))
            return self.form_invalid(form)
        Vote.objects.create(
                voting = self.voting,
                candidate = candidate
                )
        self.voting.voters.add(self.person)
        self.voting.save()
        return super(VotesView, self).form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        self.getvoting()
        if not self.voting:
            return NoVotesAtTheMomentView.as_view()(request, *args, **kwargs)
        if hasattr(request.user, 'person') and request.user.person.pk in list(self.voting.voters.all().values_list('pk', flat = True)):
            return VotesSuccessView.as_view()(request, *args, **kwargs)
        return super(VotesView, self).dispatch(request, *args, **kwargs)
