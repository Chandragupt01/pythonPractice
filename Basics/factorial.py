a=int(input("Enter a number: "))
factorial=1
while a>0:
    factorial=factorial*a
    a-=1

print(f"The factorial of {a} is {factorial}")