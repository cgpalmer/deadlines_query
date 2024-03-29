from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CsvForm
from .models import Csv, School, Assessment, Course
import os
import csv
from django.core import serializers
from ics import Calendar, Event   


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
                        try:
                            school_query = School.objects.get(school_code=school_code)
                        except School.DoesNotExist:
                            School.objects.create(name=school_name, school_code=school_code)
                        try:
                            course_query = Course.objects.get(course_code=course_code)
                        except Course.DoesNotExist:
                            Course.objects.get_or_create(course_code=course_code, course_name=course_name, 
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



def query_deadlines(request, number_of_courses):
    number_of_courses = number_of_courses
    school = School.objects.all()
    course = Course.objects.all()
    number_of_courses_array = []
    for i in range(number_of_courses):
        number_of_courses_array.append(i)
    
    context = {
        'schools': school,
        'courses': course,
        'number_of_courses': number_of_courses,
        'number_of_courses_array': number_of_courses_array  
    }

    return render(request, 'managing_deadlines/query_timetable.html', context)


def query_timetable(request):
    school_code = None
    course_code = None
    if request.method == 'POST':
        number_of_courses = request.POST.get('number_of_courses')
        print("below is the number of courses")
        print(number_of_courses)
        number_of_courses = int(number_of_courses)
        list_of_queries = []
        list_of_date_from_query = []
        
        
        list_of_course_codes = []
        list_of_assessment_name = []
        list_of_item_name = []
        list_of_deadline_dates = []
        list_of_deadline_times = []

        for i in range(number_of_courses):
            school_code = request.POST.get(f'school_select_{i}')
            print(school_code)
            course_code = request.POST.get(f'course_select_{i}')
            print(course_code)
            assessment = Assessment.objects.filter(school_code=school_code, course_code=course_code)
            list_of_queries.append(assessment)
          
            
            
            for assess in assessment:
                list_of_course_codes.append(assess.course_code)
                list_of_assessment_name.append(assess.assessment_name)
                list_of_item_name.append(assess.item_name)
                list_of_deadline_dates.append(assess.deadline_date)
                list_of_deadline_times.append(assess.deadline_time)
                if assess.deadline_date in list_of_date_from_query:
                    pass
                else:
                    list_of_date_from_query.append(assess.deadline_date)
            
                

        
        c = Calendar()
        print(len(list_of_course_codes))
        for item in range(len(list_of_course_codes)):
            print("this is the item loop")
            print(item)
            e = Event()
            e.name = f'{list_of_course_codes[item]} - {list_of_assessment_name[item]} {list_of_item_name[item]}'
            e.begin = f'{list_of_deadline_dates[item]} {list_of_deadline_times[item]}'
            c.events.add(e)
            
            c.events
        # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
        with open('my deadlines.ics', 'w') as my_file:
             my_file.writelines(c)
        print(list_of_date_from_query)
        list_of_date_from_query.sort()
        print(list_of_date_from_query)


        # By date
        list_of_queries_by_date = []

        for i in range(len(list_of_date_from_query)):
            deadline_date = list_of_date_from_query[i]
        
            assessment_by_date = Assessment.objects.filter(deadline_date=deadline_date)
            list_of_queries_by_date.append(assessment_by_date)
        context = {
            'school_code': school_code,
            'course_code': course_code,
            'list_of_queries': list_of_queries,
            'list_of_queries_by_date': list_of_queries_by_date
        }
 
    return render(request, 'managing_deadlines/results.html', context)

def number_of_courses(request):
    number_of_courses = None
    if request.method == 'POST':
        number_of_courses = request.POST.get('number_of_courses')
        print(number_of_courses)
        return redirect('query_deadlines', number_of_courses=number_of_courses)
    else: 
        schools = School.objects.all()
        context ={
            'schools': schools
        }
        return render(request, 'managing_deadlines/number_of_courses.html', context)

def search_by_school(request):
    if request.method == 'POST':
        school_code = request.POST.get('assess_by_school')
        by_school_query = Assessment.objects.filter(school_code=school_code).order_by('deadline_date')

    context = {
        'by_school_query': by_school_query,
    }
 
    return render(request, 'managing_deadlines/results_whole_school.html', context)