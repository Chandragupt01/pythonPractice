#Create a string made of the middle three characters
'''Write a program to create a new string made of the middle three characters of an input string.
Given:
Case 1
str1 = "JhonDipPeta"

Output
Dip'''

def getMiddleThreeChar(str):
    l=len(str)

    m=int(l/2)
    str2 = str[m-1:m+2]
    print(str2)

str=input("Enter a string: ")
getMiddleThreeChar(str)