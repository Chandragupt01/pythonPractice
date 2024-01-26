# Reverse a list in Python
'''Reverse a list in Python'''

list1=[]
n=int(input("Enter the length of list: "))
for i in range(n):
    item=int(input("Enter a number: "))
    list1.append(item)
revList=list1[::-1]  # orlist1.reversed()
print("Original List: ", list1)
print("Reversed List",revList)