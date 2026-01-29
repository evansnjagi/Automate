# Import modules
import logging

logging.basicConfig(filename= "myProgramLogfile.txt", level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug("Starting the program")

x = int(input("Enter number: "))
logging.debug("Get user's input")
def f(x):
    # Base case
    if x == 0:
        logging.debug(f"Recursive base case")
        return 1
    logging.debug(f"Recursion: {x}")
    return x * f(x - 1)
    logging.debug("Ending the function")

print(f"Factorial of {x} is: {f(x)}")