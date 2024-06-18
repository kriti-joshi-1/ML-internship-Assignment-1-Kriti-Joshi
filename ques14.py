'''
Write a program that reads multiple lines of input from the user until they 
enter an empty line, then prints all the lines
'''
lines = []
while True:
     line = input("enter the line : \n")
     if line == "":
          break
     lines.append(line)
for i in lines : 
     print(i)