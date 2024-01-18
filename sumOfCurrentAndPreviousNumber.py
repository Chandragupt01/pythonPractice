# Print the sum of the current number and the previous number
'''Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.'''

def SumOfCurrentAndPrev(n):
    PreviousNumber=0
    for i in range(n):
        sum = PreviousNumber + i
        print("Current Number: ",i , "Previous Number: ",PreviousNumber, "Sum: ",sum)
        PreviousNumber=i


n = int(input("Enter the Range: "))
sum=SumOfCurrentAndPrev(n)


