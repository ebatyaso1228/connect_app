from django.urls import path
from .views import ConnectList

urlpatterns = [
    path('list/', ConnectList.as_view()),
]
