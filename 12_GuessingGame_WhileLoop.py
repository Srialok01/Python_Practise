"""
Problem statement : Set a secret no , Ask people to guess the secret no in 3 Chances,
If guessed correctly print - You are right else print you are out of chances
"""

secret_Number = 9
guess_count = 3
guess_chance = 0
while guess_chance < guess_count:
    answer = int(input(" Guess the number between 1 to 9 :"))
    guess_chance += 1
    if answer == secret_Number:
        print("Whoaaa !!! You guessed it right ")
        break

else:
    print(" You are out of chances !!!")
