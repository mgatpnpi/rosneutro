from django.conf.urls import include, url, patterns
from .views import NewsView, NewsPostView

urlpatterns = patterns('news.views',
    url(r"^post/(?P<pk>\d+)/?$", NewsPostView.as_view(), name="news_post"),
    url(r"^(?P<page>\d+)/?", NewsView.as_view(), name="news")
)
