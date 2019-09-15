"""
Problem - Create a program that inputs weight , then prompts for the
weight units as - Kg/lbs
and correspondingly converts to equivalent other unit.

"""
weight = input("Enter your weights : ")
weight = int(weight)
units_weight = input("Is this in (L)bs or (K) : ")
if units_weight.upper() == 'L':
    weight_kg = weight * 0.45
    print(" Your weight is " + str(weight_kg) + "Kg")
elif units_weight.upper() == 'K':
    weight_lbs = 2.20 * weight
    print(" Your weight is " + str(weight_lbs) + "pounds")
else:
    print(" Incorrect option provided  ")
