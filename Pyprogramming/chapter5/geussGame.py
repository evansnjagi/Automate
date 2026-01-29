# Implementing a geuss game program
# Import modules
import random 
import logging

# Instantiating logging
logging.basicConfig(filename= "geussGameLogs.txt", 
                   level=logging.DEBUG, 
                   format='%(asctime)s -  %(levelname)s -  %(message)s')
# Get user's input 
logging.debug("Starting the program")
name = input("What is your name: ")
logging.debug(f"Getting user's name as input: {name}")
print(f"Hi, {name}, I am thinking of a number between 1 and 20.")
print("Take a Geuss!")

# Random geuss
secretNumber = random.randint(1, 20)
logging.debug(f"Getting the random secret integer: {secretNumber}")
for i in range(6):
    geuss = input("Enter Geuss: ")
    try:
        geuss = int(geuss)
        logging.debug(f"Getting user's geuss {geuss}")
        if geuss < secretNumber:
            print("Your geuss is too high!")
            logging.debug(f"Geuss: {geuss} < secret: {secretNumber}")
        elif geuss > secretNumber:
            print("Your geuss is too high")
            logging.debug(f"Geuss: {geuss} > secret: {secretNumber}")
        else:
            logging.info("The guess == secret number")
            break
    except Exception as err:
        logging.error("Entered a string instead of a number")
        print(f"Use an integer. You used {geuss}")

logging.info("Start game check")
if geuss == secretNumber:
    print(f"{name}, you got the secret number in {i} trials.")
else:
    print(f"Failed. The correct geuss was {secretNumber}")
logging.info("Done! project end.")