# Price of House is  1,000,000
price_house = 1000000
is_goodCredit = False
"""
If credit amount is good please provide discount of 10 % , else provide discount of 20 %
"""

if is_goodCredit:
    credit_deduction = 0.1 * price_house
    newAmount = price_house - credit_deduction
    print(newAmount)

else:
    cred_ded2 = 0.2 * price_house
    newAmount = price_house - cred_ded2
    print(newAmount)
