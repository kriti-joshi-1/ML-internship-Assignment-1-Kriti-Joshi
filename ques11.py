'''
Write a python program that generates the first n numbers in the 
Fibonacci sequence.
'''
n = int(input("enter the number n : "))
a , b = 0,1
print("The first",n,"numbers in the Fibonacci sequence are :")
for i in range(n):
     print(a, end=" ")
     a, b = b, a + b
     print()  # for a new line
     