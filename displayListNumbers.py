#  Display numbers from a list using loop
'''Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop'''

number=[12,75,150,189,145,525,50]
for num in number:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num%5==0:
        print(num)