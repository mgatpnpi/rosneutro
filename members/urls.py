from django.conf.urls import include, url, patterns
from .views import RegistrationView, \
    RegistrationSuccessView, \
    ConfirmEmailView, \
    MembersListView, \
    MemberEnterView, \
    MemberRequestSessionView, \
    MemberRequestSessioniSuccessView, \
    MemberLogoutView

urlpatterns = patterns('members.views',
    url(
        r"^register/?$",
        RegistrationView.as_view(),
        name="members_registration"
        ),
    url(
        r"success/?$",
        RegistrationSuccessView.as_view(),
        name = "members_success"
        ),
    url(
        r"^confirm/(?P<random_string>[\w\d]+)/?$",
        ConfirmEmailView.as_view(),
        name="members_email_confirm"
        ),
    url(
        r"^list/?$",
        MembersListView.as_view(),
        name="members_list"
        ),
    url(
        r"^request/session/?$",
        MemberRequestSessionView.as_view(),
        name="member_request_session"
        ),
    url(
        r"^request/session/success?$",
        MemberRequestSessioniSuccessView.as_view(),
        name="member_request_session_success"
        ),
    url(
        r"^enter/(?P<secret>[\w\d]+)/?$",
        MemberEnterView.as_view(),
        name="member_enter"
        ),
    url(
        r"^logout/?$",
        MemberLogoutView.as_view(),
        name="member_logout"
        )
)
