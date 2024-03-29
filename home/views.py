from django.shortcuts import render, redirect
import pandas as pd
from .forms import UploadFileForm, EngagementForm
import os.path
import numpy as np
import math
import os
from ics import Calendar, Event

# Create your views here.
def index(request):
    # c = Calendar()
    # e = Event()
    # e.name = "My cool event"
    # e.begin = '2014-01-01 00:00:00'
    # c.events.add(e)
    # c.events
    # # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
    # with open('my.ics', 'w') as my_file:
    #     my_file.writelines(c)
    # and it's done !
        # # Grouping the dates

        # deadline.insert(loc=len(deadline.columns), column="Date_count", value="pending", allow_duplicates=False)
        # deadline = deadline[deadline['Course Name']==str(input1)]

        # date_analysis = list(deadline['Date'].unique())


        # for date_number in range(len(date_analysis)):
        #     deadline_by_date = deadline.loc[deadline['Date'] == date_analysis[date_number]]
        #     return_count = deadline_by_date.count()
        #     deadline.loc[(deadline['Date'] == date_analysis[date_number]),'Date_count']=str(return_count['Date'])
        # deadline = deadline.sort_values(by=['Date_count', 'Date'], ascending=True)
        # print(deadline)
        
        # deadline.to_csv(index=False, path_or_buf="student_version.csv")

        # No user input - office version



        # compression_opts = dict(method='zip',
        #                         archive_name='out.csv')  
        # deadline.to_csv('out.zip', index=False,
        #           compression=compression_opts)
        
        # deadline.to_csv(index=False, path_or_buf="office_sorted.csv")
        



    form = UploadFileForm()
    context = {
      
        'form':form
    }
    return render(request, 'home/index.html', context,)

def handle_uploaded_file(f):
    with open(f'upload_folder/{f}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            handle_uploaded_file(f)
            writing_result(f)
            return redirect('home')
    else:
        form = UploadFileForm()
    return redirect('home')

def writing_result(f):
    deadline = pd.read_csv(f'upload_folder/{f}') 
    deadline.insert(loc=len(deadline.columns), column="Date_count", value="pending", allow_duplicates=False)

    date_analysis = list(deadline['Date'].unique())

    for date_number in range(len(date_analysis)):
        deadline_by_date = deadline.loc[deadline['Date'] == date_analysis[date_number]]
        return_count = deadline_by_date.count()
        deadline.loc[(deadline['Date'] == date_analysis[date_number]),'Date_count']=str(return_count['Date'])

    deadline['Date_count'] = deadline['Date_count'].str.replace('pending', "0")
    deadline['Date_count'] = deadline['Date_count'].astype(int)
    deadline = deadline.sort_values(by=['Date_count', 'Date'], ascending=[False, False])
   
    deadline_table = deadline.to_html(index=False)
    text_file = open("templates/includes/result.html", "w")
    text_file.write(deadline_table)
    text_file.close()


def engage_upload(request):
    if request.method == 'POST':
        form = EngagementForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            handle_uploaded_file(f)
            writing_engage_result(f)
            return redirect('download_ready')
    else:
        form = EngagementForm()
    return redirect('engagement')

def writing_engage_result(f):
    doc_name = f"upload_folder/{f}"
    print(doc_name)
    doc_name = doc_name.split("/")
    print(doc_name)
    doc_name = doc_name[1]
    doc_name = doc_name.split(".")
    print(doc_name)

    data = pd.read_csv(f"upload_folder/{f}")
    if 'Lateness (H:M:S)' in data.columns:
        data = data[['Email', 'Total Score']]
    elif 'Institution' in data.columns:
        data = data.iloc[:, [5, 6]] # change to index 6 and 7
    else:
        data = data.iloc[:, [2, 6]]
    
    data.columns = ['UUN', 'ATTENDED']
    data['UUN'] = data['UUN'].str.replace('@ed.ac.uk','')
    data['ATTENDED'].fillna('-1', inplace=True)
    data['ATTENDED'] = data['ATTENDED'].astype(str)
    data.loc[(data['ATTENDED'] == 'Needs Marking'), 'ATTENDED'] = '+'
    data['ATTENDED'] = data['ATTENDED'].str.replace('-','-2')
    data['ATTENDED'] = data['ATTENDED'].str.replace('+','2')
    data['ATTENDED'] = data['ATTENDED'].astype(float)
    data.loc[(data['ATTENDED'] > -1), 'ATTENDED'] = 'Y'
    data.loc[(data['ATTENDED'] != 'Y'), 'ATTENDED'] = 'N'
    data.insert(2, "DESCRIPTION", f"{doc_name[0]}")
    data.insert(3, "NOTES", "")
    data.insert(1, "ORGANISER", "")
    data.insert(1, "EVENT_DATE", "") # filename
    data.insert(1, "EVENT_TYPE", "CRSWRK")
    
    data.to_csv(index=False, path_or_buf=f"static/staticfiles/{f}")
    fetch_download = f"static/staticfiles/{f}"

    print(data)
    return fetch_download

def engagement(request):
    

    form = EngagementForm()
    context = {
      
        'form':form
    }
    return render(request, 'home/engagement.html', context,)


def download_ready(request):
    for filename in os.listdir('static/staticfiles/'):
        print(filename)
        download =  f'staticfiles/{filename}'
    context = {
        'download': download
    }
    return render(request, 'home/download_ready.html', context)