'''
QUES 25: 
Write a program that copies the contents of one text file to another
'''
f1 = open("file1.txt","r")
f2 = open("file2.txt","w")
f2.write(f1.read())