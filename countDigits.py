# Count the total number of digits in a number
'''Write a program to count the total number of digits in a number using a while loop.'''

num=int(input("Enter a number: "))
counter=0
while num!=0:
    num=num//10
    counter+=1
print(counter)