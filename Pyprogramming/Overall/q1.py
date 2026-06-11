# Question 1: Solution

# Text 
text = "  John,Doe,30  "

# Split
first_name, last_name, age = text.strip().split(",")

# Solution
print(f"Name: {first_name} {last_name}, Age: {age} ")