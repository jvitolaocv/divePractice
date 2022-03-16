from django import forms
from django.contrib import admin

from taxonomy.models import Topic


class TopicForm(forms.ModelForm):
    model = Topic
    fields = ['display_name', 'internal_name']


class TopicAdmin(admin.ModelAdmin):
    form = TopicForm
    list_display = ['display_name', 'internal_name']
    readonly_fields = ['site']


admin.site.register(Topic, TopicAdmin)
