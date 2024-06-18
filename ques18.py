'''
QUES 18 : 
Write a python program that checks if two strings are anagrams of each other
'''
str1 = input("enter first string : ")
str2 = input("enter second string : ")
count1 = {}
count2 = {}
for char in str1:
     if char in count1:
          count1[char] += 1
     else:
          count1[char] = 1
for char in str2:
     if char in count2:
          count2[char] += 1
     else:
          count2[char] = 1

if sorted(count1) == sorted(count2):
     print("The strings are anagrams of each other")
else : 
     print("The strings are not anagrams of each other")