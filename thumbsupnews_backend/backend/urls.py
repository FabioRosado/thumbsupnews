from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views


router = DefaultRouter()
router.register("headlines", views.HeadlinesList, "/headlines")
router.register("markets", views.MarketsList, "/markets")
router.register("popular", views.PopularArticles, "/popular")
router.register("contact", views.ContactCreate)
router.register("sentiment", views.ClassifySentence)
router.register("summary", views.Summary)

urlpatterns = [
    path("", include(router.urls)),
]
