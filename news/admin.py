from django.contrib import admin
from pages.admin import TranslationInlineMixin
from .models import NewsPost, NewsPostTranslation

class NewsPostTranslationInline(TranslationInlineMixin, admin.StackedInline):
    model = NewsPostTranslation
    
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created', 'modified', 'published')
    list_editable = ('published', )
    inlines = [NewsPostTranslationInline,]

admin.site.register(NewsPost, NewsPostAdmin)
