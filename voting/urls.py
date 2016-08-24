from django.conf.urls import include, url, patterns
from .views import VotesView, VotesSuccessView

urlpatterns = patterns('voting.views',
        url(
            r"^current/?$",
            VotesView.as_view(),
            name = "votes"
            ),
    )

