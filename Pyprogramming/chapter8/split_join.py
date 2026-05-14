# Message
message = "I love Data Science"

# Split a text
split_message = message.split()

# Convert to lowercase
convert_message = [message.lower() for message in split_message]

# Join the list into a string
joined_string = " ".join(convert_message)
print(joined_string)