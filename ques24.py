'''
QUES 24 : 
Write a program that acts as a simple calculator. It should take two 
numbers and an operator (+, -, *, /) as input and print the result.
'''

n1 = int(input("enter the first number : "))
n2 = int(input("enter the second number : "))
ch = (input("enter the operator : "))
if ch == "+":
     print(n1 + n2)
elif ch == "-":
     print(n2 - n1)
elif ch == "*":
     print(n1 * n2)
elif ch == "/":
     print(n1 / n2)

else : 
     print("Invalid operator")