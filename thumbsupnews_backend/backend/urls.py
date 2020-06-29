from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views


router = DefaultRouter()
router.register("headlines", views.HeadlinesList, "/headlines")
router.register("markets", views.MarketsList)
router.register("contact", views.ContactCreate)
router.register("sentiment", views.ClassifySentence)

urlpatterns = [
    path("", include(router.urls)),
]
