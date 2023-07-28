import pandas

data = pandas.read_csv('004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

gray_count = 0
red_count = 0
black_count = 0

fur = data["Primary Fur Color"]

for x in fur:
    if x == 'Gray':
        gray_count += 1
    elif x == 'Cinnamon':
        red_count += 1
    elif x == 'Black':
        black_count += 1

squirrels = {
    'fur color':['gray','red','black'],
    'count' : [gray_count,red_count,black_count],
}

converted_data = pandas.DataFrame(squirrels)
converted_data.to_csv('my_data.csv')  