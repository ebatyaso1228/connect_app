from django.urls import path
from .views import ConnectList , ConnectDetail , ConnectCreate , ConnectDelete , ConnectUpdate

urlpatterns = [
    path('list/', ConnectList.as_view(), name='list'),
    path('detail/<int:pk>',ConnectDetail.as_view(), name='detail'),
    path('create/', ConnectCreate.as_view(), name='create'),
    path('delete/<int:pk>', ConnectDelete.as_view(), name='delete'),
    path('update/<int:pk>', ConnectCreate.as_view(), name='update'),
]
