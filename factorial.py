#Find the factorial of a given number
'''Write a program to use the loop to find the factorial of a given number.'''

num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial of negative number does not exists")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print(factorial)