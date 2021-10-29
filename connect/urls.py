from django.urls import path
from .views import connect

urlpatterns = [
    path('a/',connect),
]
