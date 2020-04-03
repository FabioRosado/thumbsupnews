from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import Headline
from backend.serializers import HeadlineSerializer

@csrf_exempt
def headline_list(request):
    if request.method == 'GET':
        headline = Headline.objects.all()
        serializer = HeadlineSerializer(headline, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HeadlineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def headline_detail(request, pk):
    """
    Retrieve, update or delete a headline. 
    """
    try:
        headline = Headline.objects.get(pk=pk)
    except Headline.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = HeadlineSerializer(headline)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HeadlineSerializer(headline, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        headline.delete()
        return HttpResponse(status=204)