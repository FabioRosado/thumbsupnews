from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView

from backend.models import Headline, Contact, Sentiment, Summary
from backend.serializers import (
    HeadlineSerializer,
    ContactSerializer,
    SentimentSerializer,
    SummarySerializer
)


@method_decorator(cache_page(60 * 60 * 6), name="list")
class MarketsList(viewsets.ModelViewSet):
    queryset = Headline.objects.filter(
        Q(categories__icontains="markets")
        | Q(categories__icontains="commodities")
        | Q(categories__icontains="money")
        | Q(categories__icontains="stocks")
    )
    serializer_class = HeadlineSerializer


@method_decorator(cache_page(60 * 60 * 6), name="list")
class HeadlinesList(viewsets.ModelViewSet):
    queryset = Headline.objects.all().order_by("-date")
    serializer_class = HeadlineSerializer
    filterset_fields = ["categories", "source", "sentiment", "is_positive", "date", "clicks"]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["categories"]

    def perform_create(self, serializer):
        serializer.save()


@method_decorator(cache_page(60 * 60 * 6), name="list")
class PopularArticles(viewsets.ModelViewSet):
    queryset = Headline.objects.all().order_by("-clicks")
    serializer_class = HeadlineSerializer
    filterset_fields = ["categories", "source", "sentiment", "is_positive", "date", "clicks"]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["categories"]


class ContactCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save()


class ClassifySentence(viewsets.ModelViewSet):
    queryset = Sentiment.objects.all()
    serializer_class = SentimentSerializer

    def perform_create(self, serializer):
        serializer.save()


class Summary(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

    def perform_create(self, serializer):
        serializer.save()