n=int(input("Enter the number: "))
m=n
order=len(str(n))
total=0
while m>0:
    digit=m%10
    total+=digit**order
    m=m//10
if total==n:
    print("Armstrong number")
else:
    print("Not Armstrong number")