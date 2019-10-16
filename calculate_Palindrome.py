"""
Calculate if given no is palindrome or not
"""

def palindorme(num):
    if num == num[::-1]:
        print("palindrome")
    else:
        print("Not palindrome")


number = input("Enter the number:")
palindorme(number)
