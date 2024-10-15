a=int(input("Enter a number: "))
totalFactors=0
for i in range(2,a):
    if a%i==0:
        totalFactors+=1

if totalFactors==0:
    print("Is a primenumber")
else:
    print("not a primenumber")