#! /usr/bin/env python3
import csv
import sys

def populate_dictionary(filename):
  """Populate a dictionary with email addresses and full names from a CSV file"""
  email_dict = {}
  with open(filename, newline='') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
      email_dict[row[0]] = row[1]
  return email_dict

def find_email(argv):
  """Return an email address based on the username given"""
  # Create the username based on the command line input
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('C:/Users/jinch/mi-portafolio-python/python-scripts/email_test/user_emails.csv')
    # Find and print the email
    if email_dict.get(fullname):
       return email_dict.get(fullname)
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"

print(find_email(sys.argv))