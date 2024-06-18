'''
QUES 5 :
Write a program that takes a string input from the user and writes it to a text file
'''
file = open("ques5.txt","w")
user_input = input("Enter a string: ")
file.write(user_input)