from django.contrib import admin
from django.urls import path, include
from .views import WarriorAPIList, WarriorAPIUpdate, WarriorAPIDestroy
from rest_framework import routers


urlpatterns = [
    path('api/v1/warrior/', WarriorAPIList.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/warrior_update/<int:pk>/', WarriorAPIUpdate.as_view()),
    path('api/v1/warrior_delete/<int:pk>/', WarriorAPIDestroy.as_view()),


    path('messages-drf/', include("django_messages_drf.urls", namespace="django_messages_drf")),
    path('friendship/', include('friendship.urls')),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),



    # path('api/v1/warrior_list/', WarriorViewSet.as_view({'get': 'list'})),
    # path('api/v1/warrior_list/<int:pk>/', WarriorViewSet.as_view({'put': 'update'})),
]