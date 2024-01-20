# Calculate income tax for the given income by adhering to the rules below
'''Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
For example, suppose the taxable income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.'''

def incomeTax(income):
    tax=0
    if income<=10000:
        tax=0
    elif income<=20000:
        tax=(income-10000)*(10/100)
    else:
        tax=0

        tax=(10000)*(10/100)

        tax+=(income-20000)*(20/100)
    print(tax)

income=int(input("Enter your income: "))
incomeTax(income)