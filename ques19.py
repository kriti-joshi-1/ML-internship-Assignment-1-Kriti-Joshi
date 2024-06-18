'''
QUES 19 : 
Write a python program that removes all punctuation from a given string.
'''

str = input("enter the string : ")
str2 = ''
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in str: 
     if i in punctuation:
          pass
     else : 
          str2 += i
print(str2)

