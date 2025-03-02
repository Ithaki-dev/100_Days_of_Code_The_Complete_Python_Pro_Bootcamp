#ScriptFile for processing csv
import os
import csv
import pandas

data_list = []
current_path = os.path.dirname(__file__)
file_path = current_path + '\weather_data.csv'
temperature =[]
# My solution
# def read_csv(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             data_list.append(line.strip().split(','))
#     return data_list

# if __name__ == '__main__':
#     read_csv(file_path)
#     print(data_list)
# my other solution
# def process_csv(file_path):
#     with open(file_path, 'r') as file:
        
#         reader = csv.DictReader(file)
#         for row in reader:
#             data_list.append(row)
#             print(row)
#             temperature.append(int(row['temp']))
#     return data_list

# if __name__ == '__main__':
#     process_csv(file_path)

#     print(temperature)

#Using pandas library
def process_csv_pandas(file_path):
    df = pandas.read_csv(file_path)
    
    return df

if __name__ == '__main__':
    data = process_csv_pandas(file_path)
    print(data)
    print(data['temp'])
    # print(data['temp'].mean())
    # print(data['temp'].max())
    # print(data['temp'].min())
    # print(data['temp'].std())
    # print(data['condition'])

    #get data in row 1
    # print(data[data.day == "Monday"])

    # get the row with the highest temperature
    # print(data.loc[data['temp'].idxmax()])

    #Convert monday temperature to fahrenheit
    monday_temp = data[data.day == "Monday"]
    monday_temp_f = monday_temp['temp'] * 9/5 + 32
    print(f"The temperature on Monday in Fahrenheit is: {monday_temp_f.values[0]}")

    #Create a dataframe from scratch
    data_dict = {
        'students': ['Amy', 'James', 'Angela'],
        'scores': [76, 56, 65]
    }
    df = pandas.DataFrame(data_dict)
    print(df)
    
    # read 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250302.csv file and
    # count the number of squirrels in each color
    squirrel_file_path = current_path + '\Squirrel_census.csv'
    squirrel_data = pandas.read_csv(squirrel_file_path)
    print(squirrel_data)
    squirrel_color = squirrel_data['Primary Fur Color'].value_counts()
    print(squirrel_color)
    df = pandas.DataFrame(squirrel_color)
    df.to_csv(current_path + '\squirrel_count.csv')
