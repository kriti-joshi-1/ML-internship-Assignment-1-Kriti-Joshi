'''
QUES 8 : 
Write a python program that concatenates two strings and returns the 
result.
'''

def concatenate_strings(s1, s2):
     return s1 + s2
s1 = input("enter the first string : ")
s2 = input("enter the second string : ")
print("The concatenated string is : ",concatenate_strings(s1, s2))