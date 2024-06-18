'''
Write a python program that calculates the sum of the digits of a given 
number.
'''

n = input("enter the number : ")
sum = 0
for i in n:
     sum += int(i)
print("sum of the digits of the number is ",sum)