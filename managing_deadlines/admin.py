from django.contrib import admin
from .models import Csv, School, Assessment, Course
# Register your models here.
# register all the models here so things can be easily changed. 
admin.site.register(Csv)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(Assessment)
