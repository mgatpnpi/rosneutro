from django.conf.urls import include, url, patterns
from .views import PreVotesView, PreVotesSuccessView, VotesView, VotesSuccessView

urlpatterns = patterns('voting.views',
        url(
            r"^current/?$",
            VotesView.as_view(),
            name = "votes"
            ),
        url(
            r"^propose/?$",
            PreVotesView.as_view(),
            name = "prevotes"
            ),
    )

