# Display numbers divisible by 5 from a list
'''Iterate the given list of numbers and print only those numbers which are divisible by 5'''

n=int(input("Enter the size of the list: "))
numList = []
for i in range(n):
    x=int(input("Enter a number: "))
    numList.append(x)
print(numList)

for x in numList:
    if x % 5 ==0:
        print(x)