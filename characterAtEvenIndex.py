# Print characters from a string that are present at an even index number
'''Write a program to accept a string from the user and display characters that are present at an even index number.'''

s = input("Enter a string : ")
length = len(s)
for i in range(0,length-1,2):
    print(s[i])