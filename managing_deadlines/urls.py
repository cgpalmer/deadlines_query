from django.urls import path
from . import views


urlpatterns = [
    path('csv_upload/', views.upload_csv, name='upload_csv'),
    path('queries/', views.query_deadlines, name='query_deadlines'),
    path('results/', views.query_timetable, name='query_timetable'),
]