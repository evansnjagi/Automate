# Implement a spike program 

# Modules
import time, sys

try:
    while True:
        for i in range(9):
            print("-" * i * i)
            time.sleep(0.5)
        for i in range(7, 1, -1):
            print("-" * i * i)
            time.sleep(0.5)
except KeyboardInterrupt:
    sys.exit()