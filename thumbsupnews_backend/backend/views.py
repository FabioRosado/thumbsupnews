from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework.response import Response

from backend.models import Headline
from backend.serializers import HeadlineSerializer


# @method_decorator(name="GET")
class HeadlinesList(viewsets.ModelViewSet):
    
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    filterset_fields = ['categories', 'source', 'sentiment', 'is_positive', 'date']
    
    def perform_create(self, serializer):
        serializer.save()
