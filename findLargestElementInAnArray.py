#Python Program to Find Largest Element in an Array
'''To find the largest element in an array, iterate over each element and compare it with the current largest element. If an element is greater, update the largest element. At the end of the iteration, the largest element will be found.

Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20
Input : arr[] = {20, 10, 20, 4, 100}
Output : 100'''

arr=[10, 324, 45, 90, 9808]
largestElement=arr[0]
for element in arr:
    if element>largestElement:
        largestElement=element
    else:
        continue
print(largestElement)