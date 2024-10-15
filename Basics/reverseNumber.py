a=int(input("Enter a number: "))
b=a
n=0
while b>0:
    digit=b%10
    n=(n*10)+digit
    b=b//10

print(f"The reverser of {a} is {n}")