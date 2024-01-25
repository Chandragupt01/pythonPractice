# Arrange string characters such that lowercase letters should come first
'''Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.'''

str=input("Enter a string: ")
sLower=''
sUpper=''
for i in str:
    if i.islower():
        sLower+=i
    else:
        sUpper+=i
print(sLower+sUpper)