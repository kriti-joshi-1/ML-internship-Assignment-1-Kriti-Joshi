'''
Write a program that reads data from a CSV file and prints it to the console.
'''
import csv
file = open("ques15.csv","r+")
reader = csv.reader(file)
try : 
     for row in reader:
          print(row)
except Exception:
     print("Error Occured")