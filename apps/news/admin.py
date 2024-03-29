from django import forms
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from news.models import NewsPost, WhatWeAreReading
class WhatWeAreReadingForm(forms.ModelForm):
    model = WhatWeAreReading
    fields = [
        'title',
        'source',
        'link',
        'publish_date'
    ]

class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = [
        'title',
        'body',
        'source',
        'is_cover_story',
        'publish_date',
        'topics',
        'active',
    ]


class NewsPostAdmin(SummernoteModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'site', 'is_cover_story', 'active', 'has_topics']
    list_editable = ['is_cover_story', 'active']
    readonly_fields = ['site', ]
    summernote_fields = ['body', ]


class WhatWeAreReadingAdmin(SummernoteModelAdmin):
    list_display = ['title', 'source', 'link', 'publish_date']

admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(WhatWeAreReading, WhatWeAreReadingAdmin)