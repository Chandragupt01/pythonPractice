# Create a new list from two list using the following condition
'''Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.'''

list1=[10,20,30,35,50,55,80]
list2=[15,25,46,57,65,78,83]
result=[]

for i in list1:
    if i % 2 == 0:
        result.append(i)
for i in list2:
    if i % 2 != 0:
        result.append(i)
print(result)