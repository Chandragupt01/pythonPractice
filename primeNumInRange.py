# Write a program to display all prime numbers within a range
'''A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers'''

start=int(input("Enter a number: "))
end=int(input("Enter a number: "))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)