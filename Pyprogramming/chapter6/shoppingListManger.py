# Implementing a shopping list manger system
shoppingList = []
while True:
    print("\n Shopping List Manger")
    print("1. Add items")
    print("2. Remove items")
    print("3.Show list")
    print("4. Check items")
    print("5. Quit")

    # Get user's input
    choice = input("Enter your choice: ")

    if choice == "1":
        item  = input("Enter item to add: ")
        shoppingList.append(item)
        print(f"Successfully added {item} in your shopping list")