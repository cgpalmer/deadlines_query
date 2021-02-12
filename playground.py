import pandas as pd

deadline = pd.read_csv('test_data.csv')  
print(deadline)

headers = list(deadline.columns.values)

print(headers)
# Course Code,Course Name,Semester,Coursework Category,Coursework Type,Coursework Name,Date
courses = deadline['Course Code'].unique()
for i in courses:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")

course_name = deadline['Course Name'].unique()
for i in course_name:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")

semester = deadline['Semester'].unique()
for i in semester:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")

coursework_category = deadline['Coursework Category'].unique()
for i in coursework_category:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")

coursework_type = deadline['Coursework Type'].unique()
for i in coursework_type:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")

coursework_name = deadline['Coursework Name'].unique()
for i in coursework_name:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")

date = deadline['Date'].unique()
for i in date:
    print(i)
    print("Making a record to the database")
    print("Already in the database - not saved")
    print("New record added")




# When you have a database, you can enter each course name in as a separate course.