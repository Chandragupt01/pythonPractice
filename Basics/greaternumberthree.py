a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

if a>b and a>c:
    print(f"{a} is greater.")
elif b>a and b>c:
    print(f"{b} is greater.")
elif c>a and c>b:
    print(f"{c} is greater.")
else:
    print("All are equal")
