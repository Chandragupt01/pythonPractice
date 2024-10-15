a=int(input("Enter a number: "))
b=a
count=0
while b>0:
    count+=1
    b=b//10

print(f"The number of digits are {count}")