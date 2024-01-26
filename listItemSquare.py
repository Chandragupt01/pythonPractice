# Turn every item of a list into its square
'''Given a list of numbers. write a program to turn every item of a list into its square.'''

list1=[]
squaredList=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    item=int(input("Enter a number: "))
    list1.append(item)

for x in list1:
    squaredList.append(x*x)

print("Original List: ",list1)
print("Squared List: ",squaredList)