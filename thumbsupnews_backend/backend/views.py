from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from backend.models import Headline
from backend.serializers import HeadlineSerializer


class HeadlinesList(viewsets.ModelViewSet):
    
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    filterset_fields = ['categories', 'source', 'sentiment', 'is_positive', 'date']
    
    def perform_create(self, serializer):
        serializer.save()
