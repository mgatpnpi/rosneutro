from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
    url(r"^letter/?$", TemplateView.as_view(template_name = 'letter.html'), name="letter"),
)
