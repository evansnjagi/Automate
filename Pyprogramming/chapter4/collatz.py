# Implementing a collatz sequence algorithm
# Modules
import sys

# Function implementation
def collatz(number):
    while number != 1:
        print(number, end=" ")
        if  number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
    print("1")

number = input("Enter a positive integer: ")