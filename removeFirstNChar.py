# Remove first n characters from a string
'''Write a program to remove characters from a string starting from zero up to n and return a new string.'''

def remove_char(s,num):
    x=s[num:]
    return x

S=input("Enter a string: ")
num=int(input("Enter a number: "))
print(remove_char(S,num))