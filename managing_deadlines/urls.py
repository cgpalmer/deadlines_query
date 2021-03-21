from django.urls import path
from . import views


urlpatterns = [
    path('csv_upload/', views.upload_csv, name='upload_csv'),
    path('course_amount/', views.number_of_courses, name='number_of_courses'),
    path('queries/<int:number_of_courses>/', views.query_deadlines, name='query_deadlines'),
    path('results/', views.query_timetable, name='query_timetable'),
]