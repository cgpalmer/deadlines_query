from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    deadline = pd.read_csv('test_data.csv') 


    # input1 = input('Enter course name: ')
    # print("Looking for deadline data regarding " + str(input1) + ".")



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

    deadline.insert(loc=len(deadline.columns), column="Date_count", value="pending", allow_duplicates=False)

    date_analysis = list(deadline['Date'].unique())

    for date_number in range(len(date_analysis)):
        deadline_by_date = deadline.loc[deadline['Date'] == date_analysis[date_number]]
        return_count = deadline_by_date.count()
        deadline.loc[(deadline['Date'] == date_analysis[date_number]),'Date_count']=str(return_count['Date'])
    deadline = deadline.sort_values(by=['Date_count', 'Date'], ascending=False)
    print(deadline)

    # compression_opts = dict(method='zip',
    #                         archive_name='out.csv')  
    # deadline.to_csv('out.zip', index=False,
    #           compression=compression_opts)
    
    # deadline.to_csv(index=False, path_or_buf="office_sorted.csv")
    deadline_table = deadline.to_html(index=False)

    text_file = open("templates/includes/result.html", "w")
    text_file.write(deadline_table)
    text_file.close()
    context = {
        'deadline': deadline_table
    }
    return render(request, 'home/index.html', context,)