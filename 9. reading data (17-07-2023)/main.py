#Using CSV to read files. It can be tedious with complex spreadsheets
"""import csv

data = []
temperatures = []

file = open('002 weather_data.csv')
dati = csv.reader(file)
for x in dati:
    data.append(x)
file.close()

for x in data[1:]:
    temperatures.append(int(x[1]))
    
print(temperatures)"""
    

import pandas

data = pandas.read_csv('002 weather_data.csv')
print(data["temp"])

#converting to a list
temp_list = data["temp"].to_list()

#returns the mean of a row
mean = data["temp"].mean()

#headings are usually automatically covnerted into attributes. ex: data.condition/data.temp
print(data[data.temp == data["temp"].max()])


#creating a dataframe from scratch
data_dict = {
    "students" : ["Weissenberg", "Himura","Gentile"],
    "marks" : ["98","100","91"],
}

converted_data = pandas.DataFrame(data_dict)
#converted_data.to_csv(path)      > converts to a spreadsheet



#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

#iterating through rows

{new_key:new_value for index,row in data.iterrows()}