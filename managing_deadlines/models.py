from django.db import models

# Create your models here. Create assessment model here.

# Three models: schools, course, item


class Csv(models.Model):
    file_name = models.FileField(upload_to="static/staticfiles/")
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

class School(models.Model):
  
    school_code = models.CharField(max_length=10)
    name = models.CharField(max_length=254, null=False, default="Unnamed school")

    def __str__(self):
        return self.course_code


class Course(models.Model):
   
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=254, null=False, default="Unnamed course")

    def __str__(self):
            return self.course_code

class Assessment(models.Model):
    school_name = models.CharField(max_length=254, null=False, default="Unnamed assessment type")
    course_name = models.CharField(max_length=254, null=False, default="Unnamed assessment type")
    course_code = models.CharField(max_length=254, null=False, default="Unnamed assessment type")
    assessment_type = models.CharField(max_length=254, null=False, default="Unnamed assessment type")
    assessment_name = models.CharField(max_length=254, null=False, default="Unnamed assessment name")
    item_name = models.CharField(max_length=254, null=False, default="Unnamed item name")
    deadline_date = models.DateField(null=True)
    deadline_time = models.TimeField(null=True)

    def __str__(self):
        return self.assessment_name
