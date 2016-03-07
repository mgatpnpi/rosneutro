from django.conf.urls import include, url, patterns
from .views import RegistrationView, ConfirmEmailView, MembersListView, RegistrationSuccessView

urlpatterns = patterns('members.views',
    url(r"^register/?$", RegistrationView.as_view(), name="members_registration"),
    url(r"success/?$", RegistrationSuccessView.as_view(), name = "members_success"),
    url(r"^(?P<random_string>[\w\d]+)/confirm/?$", ConfirmEmailView.as_view(), name="members_email_confirm"),
    url(r"^list/?$", MembersListView.as_view(), name="members_list")
)
