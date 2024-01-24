# Reverse a given integer number
'''Reverse a given integer number'''

num=int(input("Enter a number: "))
givenNum=num
reverseNum=0
while givenNum!=0:
    reverseNum=(reverseNum*10)+(givenNum%10)
    givenNum=givenNum//10
print("Given Number: ",num, " Reversed Number: ",reverseNum)
