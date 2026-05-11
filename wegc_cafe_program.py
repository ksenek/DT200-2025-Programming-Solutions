##
# WEGC School Café Orders System
# Allows school cafe to view menu items, add new items, update & delete items, show trending items
# Miss Senek
# 2026


def view_items(items):
    """functionality to view all items stored in list"""
    
    print("\n--- Menu Items ---")
    # loop over each item that is stored in the program
    for item in items:
        print(item)


def add_item(items, name, category, orders):
    """allows user to add a new item with name, category and # of orders"""
    new_item = {"name": name, "category": category, "orders": orders}
    items.append(new_item)
    print("Item added.") # confirmation message that item has been successfully added


def update_orders(items, name, new_orders):
    """allows user to update an existing item with the number of orders"""
    
    found = False
    for item in items:
        if item["name"].lower() == name.lower():
            item["orders"] = new_orders
            print("Orders updated.")
            found = True
    if not found:
        print("Item not found.")


def delete_item(items, name):
    """allows a user to delete an item from the cafe"""
    
    for i in range(len(items)):
        if items[i]["name"].lower() == name.lower():
            del items[i]
            print("Item deleted.")
            return
    print("Item not found.") # feedback message if item is not found in list
    
    
def show_trending(items, min_orders):
    """allows the user to view trending items ie. the most popular items"""
    
    print("\n--- Trending Items ---")
    for item in items:
        if item["orders"] >= min_orders: # accepts the value inputted and above
            print(item)


if __name__ == "__main__":
    # list of dictionaries storing individual item information
    menu = [
        {"name": "Chicken Wrap", "category": "meal", "orders": 12},
        {"name": "Sausage Roll", "category": "hot food", "orders": 20},
        {"name": "Muffin", "category": "snack", "orders": 8},
        {"name": "Orange Juice", "category": "drink", "orders": 15},
        {"name": "Cookie", "category": "snack", "orders": 10}
    ]

    # loop to keep menu running until user chooses to exit
    running = True

    while running:
        print("\nSchool Café System")
        print("1. View all items")
        print("2. Add item")
        print("3. Update orders")
        print("4. Delete item")
        print("5. Show trending items")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_items(menu)

        elif choice == "2":
            name = input("Enter item name: ")
            category = input("Enter category: ")
            orders = int(input("Enter number of orders: "))
            add_item(menu, name, category, orders)

        elif choice == "3":
            name = input("Enter item name to update: ")
            new_orders = int(input("Enter new number of orders: "))
            update_orders(menu, name, new_orders)

        elif choice == "4":
            name = input("Enter item name to delete: ")
            delete_item(menu, name)

        elif choice == "5":
            min_orders = int(input("Enter minimum orders: "))
            show_trending(menu, min_orders)

        elif choice == "6":
            running = False
            print("Goodbye!")
            
        # taking invalid input into account
        else:
            print("Invalid choice, try again.")
