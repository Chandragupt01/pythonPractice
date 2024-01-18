#Calculate the multiplication and sum of two numbers
'''Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.'''

def multiplicationOrSum(num1,num2):
    product = num1*num2
    if product<=1000:
        return product
    else:
        return num1 + num2
    
num1 = 40
num2 = 30
print(multiplicationOrSum(num1,num2))