from django.urls import path
from backend import views

urlpatterns = [
    path('headlines/', views.headline_list),
    path('headlines/<int:pk>/', views.headline_detail)
]