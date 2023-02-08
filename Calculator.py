"""
Let's build a calculator for figuring out how much I owe in taxes (and by calculator, I mean function). 
Write a function that takes in a list of tuples, where each tuple contains two values, as well as an 
income to compute the taxes on (so your function should accept two arguments). For the tuple list, 
the first value of a tuple will be an income upper bound, and the second will be a tax rate for all 
income up to the given income bound. You need to build a calculator that will calculate the tax for 
all income up to each income bound (if it goes up that high) for the given tax rate. You can assume 
that the list of tuples will be sorted by the income bound (e.g. the first value in the tuple), such 
that the lowest income bound will be first, and the highest last (see below for an example).
"""

def taxCalculator(taxList, income):

    #sorts first digit of tuple
    taxList = sorted(taxList)

    #defines two important variables
    remainingIncome = income; totalTax = 0

    for bracket, tax in taxList:
        
        #if income completely clears tax bracket
        if income > bracket:
            
            #whole bracket taxed at rate
            totalTax += bracket * tax
            
            #subtracts bracket from remaining income
            remainingIncome -= bracket

        else: #last step!

            #taxes last portion at rate
            totalTax += remainingIncome * tax
            
            #breaks (no income left)
            break

    return totalTax

print(taxCalculator([(50000, 0.08), (150000, 0.15), (100000, 0.10)],  70000))
    
