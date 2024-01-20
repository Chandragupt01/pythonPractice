# Check Palindrome Number
'''Write a program to check if the given number is a palindrome number.'''

def palindrome(num):
    OriginalNumber=num
    reversedNum=0

    while num > 0:
        remainder=num%10
        reversedNum = (10*reversedNum)+remainder
        num=num//10

    if OriginalNumber==reversedNum:
        print(OriginalNumber," is a palindrome")
    else:
        print(OriginalNumber," is not a palindrome")

num=int(input("Enter a number: "))
palindrome(num)