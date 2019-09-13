from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from blog import views


app_name='blog'


urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'longgrids/(?P<slug>[a-z0-9-_]+)/$', views.longgrid_detail, name='longgrid_detail'),
    path('longgrids/', views.longgrids, name="longgrids"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
