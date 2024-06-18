'''
QUES 21 : 
Write a python program that counts the occurrences of a specific element 
in a list.
'''

s = input("enter the string to be searched : ")
ch = input("enter the char to be searched for : ")
c = 0
for i in s : 
     if i == ch : 
          c +=1
print(ch," ocuurs ",c," times in ",s)



