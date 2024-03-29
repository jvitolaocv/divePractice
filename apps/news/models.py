from bs4 import BeautifulSoup
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from taxonomy.models import Topic
from lib.sitestuff import SiteModel, current_site


class WhatWeAreReading(SiteModel):
    this_site = current_site().__str__()
    
    if this_site == 'biopharmadive.com':
        temp = True
    else:
        temp = False


    title = models.CharField(max_length=300)
    link = models.URLField(unique=temp)
    source = models.CharField(max_length=300)
    publish_date = models.DateField(default=timezone.now)


    def __str__(self):
        return '<{}> {}'.format(self.site.domain, self.title)

    def getDomain(self):
        return self.site.domain
    
class NewsPost(SiteModel):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=6000)
    source = models.URLField()
    is_cover_story = models.BooleanField(default=False)
    publish_date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)
    topics = models.ManyToManyField(Topic)


    def __str__(self):
        return '<{}> {}'.format(self.site.domain, self.title)

    @property
    def url(self):
        return reverse('newspost_detail', kwargs={'newspost_id': self.pk})

    @property
    def teaser(self):
        body_html = BeautifulSoup(self.body, 'html')
        body_html = body_html.text.replace('Dive Brief:', '')
        return body_html[:150]

    @property
    def has_topics(self):
        return self.topics.count() > 0

    @property
    def source_divesite(self):
        return self.site.name

    @classmethod
    def search(cls, topics=None, text_value=None):
        """Filters News Posts that match provided topics or text_value

            :param topics: QuerySet or List of Topic objects to filter against
            :type topics: QuerySet or List
            :param text_value: Search term to filter title or body against
            :type text_value: String

            :return: News Posts that match provided search terms
            :rtype: Queryset
        """
        results = cls.objects
        if topics:
            results = results.filter(topics__in=topics)
        if text_value:
            results = results.filter(Q(body__icontains=text_value) | Q(title__icontains=text_value))
        return set(results.all())

