'''
QUES 3 : 
Write a python program that calculates the factorial of a given number.
'''

a = int(input("enter the number"))
fac = 1
for i in range(1,a+1):
     fac *= i
print("the factorial of ", a , " is = ",fac)
