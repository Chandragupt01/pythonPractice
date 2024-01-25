# Count all letters, digits, and special symbols from a given string
'''Count all letters, digits, and special symbols from a given string'''

str=input("Enter a string: ")
characters=0
digits=0
specialCharacters=0
for char in str:
    if char.isalpha():
        characters+=1
    elif char.isdigit():
        digits+=1
    else:
        specialCharacters+=1
print("Character: ", characters, " Digits: ", digits, "Special Charcters: ",specialCharacters)