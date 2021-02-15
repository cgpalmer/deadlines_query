from django.shortcuts import render, redirect
import pandas as pd
from .forms import UploadFileForm
import os.path
# Create your views here.
def index(request):
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
    deadline = deadline.sort_values(by=['Date'], ascending=False)
 
    deadline_table = deadline.to_html(index=False)
    text_file = open("templates/includes/result.html", "w")
    text_file.write(deadline_table)
    text_file.close()
