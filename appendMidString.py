#Append new string in the middle of a given string
'''Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:

AuKellylt'''

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
length=len(s1)
mid=int(length/2)
print(s1[:mid]+s2+s1[mid:])