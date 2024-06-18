'''
QUES 20: 
Write a python program that takes a list of numbers and returns their sum.
'''

list_num = eval(input("enter the list of numbers : "))
def sum_list(lst):
     return sum(lst)
print("the sum of entered numbers is : ", sum_list(list_num))