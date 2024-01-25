# Calculate the sum and average of the digits present in a string
'''Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.'''

str=input("Enter a string: ")
cnt=0
sum=0
for char in str:
    if char.isdigit():
        sum+=int(char)
        cnt+=1
print("Sum: ",sum)
print("Average:",sum/cnt)