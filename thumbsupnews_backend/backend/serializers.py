from rest_framework import serializers
from .models import Headline, Contact


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['id', 'title', 'link', 'description', 'categories', 'source', 'sentiment', 'is_positive', 'date', 'created']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date']