from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets
from rest_framework.response import Response

from backend.models import Headline
from backend.serializers import HeadlineSerializer


@method_decorator(cache_page(60*60*6), name="list")
class HeadlinesList(viewsets.ModelViewSet):
    
    queryset = Headline.objects.all().order_by('-date')
    serializer_class = HeadlineSerializer
    filterset_fields = ['categories', 'source', 'sentiment', 'is_positive', 'date']
    
    def perform_create(self, serializer):
        serializer.save()
