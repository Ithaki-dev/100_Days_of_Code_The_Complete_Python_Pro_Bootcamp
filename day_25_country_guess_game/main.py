#ScriptFile for processing csv
import os
import csv
import pandas

data_list = []
current_path = os.path.dirname(__file__)
file_path = current_path + '\weather_data.csv'
temperature =[]

# def read_csv(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             data_list.append(line.strip().split(','))
#     return data_list

# if __name__ == '__main__':
#     read_csv(file_path)
#     print(data_list)

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

def process_csv_pandas(file_path):
    df = pandas.read_csv(file_path)
    
    return df

if __name__ == '__main__':
    data = process_csv_pandas(file_path)
    print(data)
    print(data['temp'])
    print(data['temp'].mean())
    print(data['temp'].max())
    print(data['temp'].min())
    print(data['temp'].std())