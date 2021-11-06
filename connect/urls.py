from django.urls import path
from .views import ConnectList , ConnectDetail , ConnectCreate , ConnectDelete , ConnectUpdate , signupfunc , loginfunc ,ConnectMember , goodfunc
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', ConnectList.as_view(), name='list'),
    path('detail/<int:pk>',ConnectDetail.as_view(), name='detail'),
    path('create/', ConnectCreate.as_view(), name='create'),
    path('delete/<int:pk>', ConnectDelete.as_view(), name='delete'),
    path('update/<int:pk>', ConnectCreate.as_view(), name='update'),
    path('member/', ConnectMember.as_view(), name='member'),
    path('good/<int:pk>', goodfunc, name='good'),

    
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     url(, views.index, name='index'),
#     url(, views.photoupload, name='photoupload'),
# ]