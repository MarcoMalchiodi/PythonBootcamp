import pandas

data = pandas.read_csv('002 weather_data.csv')

monday = data[data.day == "Monday"]
monday_temp = monday.temp
print(monday.temp+80)