# Format variables using a string.format() method.
'''Write a program to use string.format() method to format the following three variables as per the expected output'''

Money = 1000
quantity = 1
price = 450
statement = "He had {0} dolllars in his {1} pocket and wanted a watch of {2} dollars"
print(statement.format(Money,quantity,price))