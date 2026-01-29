# Implementing a boxprint

# Function printbox
def printBox(symbol, width, height):
    # Validate user inputs
    if len(symbol) != 1:
        raise Exception("Symbol should be a single character string")
    if width <= 2:
        raise Exception("Widht should be greater than 2")
    if height <= 2:
        raise Exception("Height should be greater than 2")
    print(symbol * width)
    for i in range(height - 2):
        print(f"{symbol} {'' * (width - 2)} {symbol}")
    print(symbol * width)

# Validating what the function is doing.
try:
    printBox("*", 4, 4)
    printBox("*", 3, 4)
    printBox("**", 4, 4)
    printBox("*", 4, 6)
    printBox("*", 1, 4)

except Exception as err:
    print(f"An exception happened: {str(err)}")