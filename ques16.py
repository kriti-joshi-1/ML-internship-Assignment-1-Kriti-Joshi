'''
QUES 16: 
Write a program in python that counts the frequency of each character in a string
'''

string = input("enter the string : ")
frequency = {}
for char in string:
     if char in frequency:
          frequency[char] += 1
     else:
          frequency[char] = 1
print(frequency)