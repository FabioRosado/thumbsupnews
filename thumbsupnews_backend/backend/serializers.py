from rest_framework import serializers
from .models import Headline, Contact, Sentiment


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = [
            "id",
            "title",
            "link",
            "description",
            "summary",
            "categories",
            "source",
            "sentiment",
            "is_positive",
            "date",
            "created",
            "clicks",
            "thumbs_up",
            "thumbs_down",
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "message", "date"]


class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        fields = ["message", "sentiment"]
