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



   # print(return_count)
    # deadline = deadline['Date count'].str.replace('pending', str(return_count['Date']), regex=True)

# print(deadline)

# print(date_analysis)
# for date in date_analysis:
#     deadline_by_date = deadline.loc[deadline['Date'] == date]
#     print(deadline_by_date)

# Finding the biggest number of dates.
# number_of_values = deadline['Date'].value_counts().max() 
# print(number_of_values)

# Find entries for specific deadlines
# deadline_by_date = deadline.loc[deadline['Date'] == '2021-03-08']
# return_count = deadline_by_date.count()
# print("Number of deadlines on this date " + str(return_count['Date']))
# print(deadline_by_date)

# Putting entries into MongoDB to be queried.
# print(entries)
# print("***********")
# for entry in range(len(entries)):
#     mongo_entry = list(entries[entry])
#     print(mongo_entry)
#     print("Enter into db: createobject(course_code=" + str(mongo_entry[0]) + ")")


# print(deadline)

# headers = list(deadline.columns.values)

# print(headers)
# Course Code,Course Name,Semester,Coursework Category,Coursework Type,Coursework Name,Date
# for j in headers:
#     unique_value = deadline[j].unique()
#     for i in unique_value:
#         print(i)
#         print("Making a record to the database")
#         print("Already in the database - not saved")
#         print("New record added")

# entries = []
# for row in deadline.itertuples(index=False):
#     # print(row)
#     entries.append(row)
    





# When you have a database, you can enter each course name in as a separate course.



# # deadline_count = []
# # for date_number in range(len(date_analysis)):
# #     deadline_by_date = deadline.loc[deadline['Date'] == date_analysis[date_number]]
# #     return_count = deadline_by_date.count()
# #     deadline_count.append("Number of deadlines on this date " + str(date_analysis[date_number]) + " = " + str(return_count['Date']))
# #     # print(deadline_by_date)

# # for i in deadline_count:
# #     print(i)