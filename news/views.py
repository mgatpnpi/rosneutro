from django.views.generic import ListView, DetailView
from pages.views import PageContextMixin
from .models import NewsPost

class NewsView(PageContextMixin, ListView):
    paginate_by = 10
    template_name = "news.html"
    context_object_name = "news"
    def get_queryset(self):
        return NewsPost.objects.filter(published = True)

class NewsPostView(PageContextMixin, DetailView):
    template_name = "news_post.html"
    context_object_name = "news_post"
    def get_queryset(self):
        return NewsPost.objects.filter(published = True)
