from django.db import models

from lib.sitestuff import SiteModel


class Topic(SiteModel):
    display_name = models.CharField(max_length=50)
    internal_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{} <{}>'.format(self.display_name, self.internal_name)
