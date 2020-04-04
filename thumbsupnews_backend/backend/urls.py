from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from backend import views


router = DefaultRouter()
router.register('headlines', views.HeadlinesList)

urlpatterns = [
    path('', include(router.urls)),
]