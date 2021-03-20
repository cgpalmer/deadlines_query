from django.urls import path
from . import views


urlpatterns = [
    path('csv_upload/', views.upload_csv, name='upload_csv'),
]