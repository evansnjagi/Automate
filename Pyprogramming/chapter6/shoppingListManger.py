# Implementing a shopping list manger system
shoppingList = []
while True:
    print("\nShopping List Manger")
    print("1. Add items")
    print("2. Remove items")
    print("3. Show list")
    print("4. Check items")
    print("5. Quit")

    # Get user's input
    choice = input("Enter your choice: ")

    if choice == "1":
        item  = input("Enter item to add: ")
        shoppingList.append(item)
        print(f"\nYou have successfully added {item} in your shopping list.")
    elif choice == "2":
        itemToRemove = input("Enter item to remove: ")
        if itemToRemove in shoppingList:
            shoppingList.remove(itemToRemove)
            print(f"{itemToRemove} removed!")
        else:
            print(f"{itemToRemove} not in the shopping list")
    elif choice == "3":
        print("Shopping list")
        for index, item in enumerate(shoppingList):
            print(f"{index}: {item}")
    elif choice == "4":
        itemToCheck = input("Enter item to check: ")
        if itemToCheck in shoppingList:
            print(itemToCheck, "is in the shopping list.")
        else:
            print(itemToCheck, "is not in the shopping list")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")