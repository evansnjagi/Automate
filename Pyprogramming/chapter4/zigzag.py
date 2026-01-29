# Implementing zigzag program and should handle keybordinteruption error gracefully

# Modules
import time, sys

# program
indent = 0
indentIncrease = True

try:
    while True:
        print(" " * indent, end = "")
        print("********")
        time.sleep(0.5)
        if indentIncrease:
            indent += 1
            if indent == 5:
                indentIncrease = False 
        if not indentIncrease:
            indent -= 1
            if indent == 0:
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()
