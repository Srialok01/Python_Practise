"""
calculate total price for Prices list :
prices = [10, 20, 30 ]
"""
prices = [10, 20, 30, 40]
total_price = 0
for price in prices:
    total_price = total_price + price
print(f'Total Price : {total_price}')

"""
Problem -  print numbers array with no of x
numbers = [5,2,5,2,2]
"""

numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#    print(number * "*")

for number in numbers:
    output = ""
    for count in range(number):
        output += "*"
    print(output)




