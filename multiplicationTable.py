#  Write a program to print multiplication table of a given number
''' Write a program to print multiplication table of a given number'''

n=int(input("enter a number: " ))
for i in range(11):
    print(n,"X",i,"=",n*i)