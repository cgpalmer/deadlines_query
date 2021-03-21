from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CsvForm
from .models import Csv, School, Assessment, Course
import os
import csv


# Create your views here.

# create view to take the csv and save the different assignments

def upload_csv(request):

    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                      
                    
                        school_name = row[0]
                        school_code = row[1]
                        course_code = row[2]
                        course_name = row[3]
                        assessment_name = row[6]
                        item_name = row[7]
                        date = row[8]
                        new_date = date.replace("/", "-")
                        time = row[9]
                        print(time)
                        School.objects.create(name=school_name, school_code=school_code)
                        Course.objects.create(course_code=course_code, course_name=course_name, 
                                                school_name=school_name, school_code=school_code)
                        Assessment.objects.create(
                            school_name=school_name, course_code=course_code, 
                            course_name=course_name, assessment_name=assessment_name, 
                            item_name=item_name, deadline_date=new_date, deadline_time=time,
                            school_code=school_code)
                
            obj.activated = True
            obj.save()
        return redirect(reverse('home'))
    else:
        form = CsvForm()
        context = {
            'form': form
        }

    return render(request, 'managing_deadlines/uploading_csv.html', context)



def query_deadlines(request):

    school = School.objects.values('school_code').distinct()
    course = Course.objects.all()
    assessment = Assessment.objects.all()

    context = {
        'schools': school,
        'courses': course,
        'assessments': assessment
    }

    return render(request, 'managing_deadlines/query_timetable.html', context)