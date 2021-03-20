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
                        # row = "".join(row)
                    
                        school_name = row[0]
                        course_code = row[1]
                        course_name = row[2]
                        assessment_name = row[5]
                        item_name = row[6]
                        date = row[7]
                        new_date = date.replace("/", "-")
    
                        print(date)
                        time = row[8]
                        School.objects.create(name=school_name)
                        Course.objects.create(course_code=course_code, course_name=course_name)
                        Assessment.objects.create(
                            school_name=school_name, course_code=course_code, 
                            course_name=course_name, assessment_name=assessment_name, 
                            item_name=item_name, deadline_date=new_date)
                
            obj.activated = True
            obj.save()
        return redirect(reverse('home'))
    else:
        form = CsvForm()
        context = {
            'form': form
        }

    return render(request, 'managing_deadlines/uploading_csv.html', context)

