from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('upload', views.upload, name='upload'),
    path('e_upload', views.engage_upload, name='engage_upload'),
    path('engage/', views.engagement, name='engagement'),
    path('download/', views.download_ready, name='download_ready'),
]


