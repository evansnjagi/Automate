# Implementation of a simple guese game
# Imports
import random 
import sys

random = random.randint(1, 20)

guese_count = 0
print("I am thinking of a number between 1 and 20. Geuse which...")

while guese_count < 7:
    # Get user's input
    guese = int(input("Enter your guese: "))
    if guese == random:
        print("Congraturaitons! You got the lucky number.")
        break
    else:
        if guese < random:
            print("Your guese is too low")
            guese_count += 1
        if guese > random:
            print("Your guese is too high")
            guese_count += 1
if guese_count > 6:
    print(f"Lost! The correct gues is: {random}")
    sys.exit()