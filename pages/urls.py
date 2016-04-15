from django.conf.urls import include, url, patterns
from .views import MessageView

urlpatterns = patterns('pages.views',
    url(r"^message/?$", MessageView.as_view(), name="message"),
)
