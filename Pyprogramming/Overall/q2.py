# Question 2: Solution

# Text
text = ["a.jpg", "b.txt", "c.csv", "d.jpg", "e.png"]


# Solution

files = [f.upper() for f in text if f.endswith((".jpg", ".png"))]

# Print
print(files)