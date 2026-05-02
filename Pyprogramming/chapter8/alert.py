# Alert program

message = "The system detected a theft at midnight"

# Search
if "theft" in message.lower():
    print("Alert: Theft detected")
else:
    print("No threat")