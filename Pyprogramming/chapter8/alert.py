# Alert program

alert_message = "The system detected a theft at midnight"

# Search
if "theft" in alert_message.lower():
    print("Alert: Theft detected")
else:
    print("No threat")