from rest_framework import serializers
from .models import Headline


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['title', 'link', 'description', 'categories', 'source', 'sentiment', 'is_positive', 'date']
