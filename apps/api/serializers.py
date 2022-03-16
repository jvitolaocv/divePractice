from rest_framework import serializers

from news.models import NewsPost


class NewsPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsPost
        fields = [
            'pk',
            'title',
            'teaser',
            'publish_date',
            'source',
        ]
