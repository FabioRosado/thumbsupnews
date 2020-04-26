from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins

from backend.models import Headline, Contact
from backend.serializers import HeadlineSerializer, ContactSerializer


@method_decorator(cache_page(60*60*6), name="list")
class HeadlinesList(viewsets.ModelViewSet):
    queryset = Headline.objects.all().order_by('-date')
    serializer_class = HeadlineSerializer
    filterset_fields = ['categories', 'source', 'sentiment', 'is_positive', 'date']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['categories'] 

    def perform_create(self, serializer):
        serializer.save()


class ContactCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def perform_create(self, serializer):
        serializer.save()