'''*********** Understanding Logical Operators************
Creating a banking application to check eligibility of loans for customers based on
high_income, good_credit and criminal_record
'''
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print("Eligible for loan")
if has_good_credit or has_high_income:
    print("Eligble for loan")
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("Loan can be provided as it doesn't has criminal record")