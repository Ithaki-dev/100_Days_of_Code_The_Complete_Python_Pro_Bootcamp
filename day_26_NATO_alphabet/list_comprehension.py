import os
import random

# Current path
current_path = os.path.dirname(__file__)

# this is an example of list comprehension

numbers = [1, 2, 3]

# this will create a new list where each element is the square of the corresponding element in the original list
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Robert"
new_name = [letter for letter in name]
print(new_name)

#this create a list of numbers that double the number in the range from 1 to 5
double_numbers = [n * 2 for n in range(1, 5)]

print(double_numbers)

# select only the nameswith 4 or less characters
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]

print(short_names)

# create a list that contains names longer than 5 characters
long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)

# a List Comprehension to create a new list that squares the list

numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# convert a list of string in to int and add in result list the even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']

list_of_ints = [int(num) for num in list_of_strings]

even_numbers = [num for num in list_of_ints if num % 2 == 0]

print(even_numbers)

# check file1.txt and file2.txt and print in result_list the nombers in comoon
with open(f"{current_path}/file1.txt") as file1:
    file1_data = file1.readlines()
    file1_numbers = [int(line.strip()) for line in file1_data]

with open(f"{current_path}/file2.txt") as file2:
    file2_data = file2.readlines()
    file2_numbers = [int(line.strip()) for line in file2_data]

result_list = [n for n in file2_numbers if n in file1_numbers]
print(result_list)

# create a dictionary from a list of names a create a ramdom score and check the passed students with scores higher than than 70

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

student_scores = {name: random.randint(1, 100) for name in names}

passed_students = {name: score for name, score in student_scores.items() if score > 70}
print(passed_students)

# create a dictionary from a sentence and calculate the number of letter in each word

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_counts = {word: len(word) for word in sentence.split()}

print(word_counts)

# create a dictionary that converts whether in celcius to fahrenheit

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp * 9/5) + 32 for day, temp in weather_c.items()}

print(weather_f)