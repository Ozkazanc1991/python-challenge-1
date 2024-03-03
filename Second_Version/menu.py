# Customer's order from food truck
order = []

# Sub menu prompt for the customer from food truck
menu_items = {
    "Hamburger": 6.99,
    "Fries": 2.99,
    "Tacos": 3.99,
    "Churros": 3.99,
    "Soda": 2.99,
    "Water": 1.99
}

# Printing the menu for the customer
while True:
    print("\nFood Truck Menu Items:")
    for index, (item, price) in enumerate(menu_items.items(), start=1):
        print(f"{index}. {item} - ${price:.2f}")

    # Ask the customer to make their selection from the menu when it is prompted
    menu_selection = input("Welcome! Please enter the number from the menu you want to order: ")

    # Input validation when the customer makes their selection from the menu
    if not menu_selection.isdigit():
        print("Invalid selection; please enter a number corresponding to what you see on the menu. ")
        continue

    # Convert the input to an integer and validate that it's from the listed menu_items
    menu_selection = int(menu_selection)
    if menu_selection < 1 or menu_selection > len(menu_items):
        print("Invalid selection; please enter a number corresponding to what you see on the menu.")
        continue

    # Get the item name the customer chooses from the menu_items list
    item_name = list(menu_items.keys())[menu_selection - 1]

    # Ask the quantity of the item the customer selects for their menu selection
    quantity = input(f"How many {item_name} do you want for your order today? (Default is 1): ")

    # Input validation for quantity the customer selects from the menu list
    try:
        quantity = int(quantity)
        if quantity <= 0:
            quantity = 1
    except ValueError:
        quantity = 1

    # Append the customer's order in dictionary format to the order list
    order.append({
        "Item name": item_name,
        "Price": menu_items[item_name],
        "Quantity": quantity
    })

    # Ask the customer if they would like to add another item to their order from the menu list
    choice = ''
    while True:
        choice = input("Would you like to add another item from the menu to your order? (y/n): ").lower()
        
        # Match-case statement
        match choice:
            case 'y':
                # Continue the order
                break
            case 'n':
                # Finish the order
                print("Thank you for your order.")
                break
            case _:
                # Invalid selection, ask the customer to try again
                print("You have made an invalid selection, please try again. Please enter either 'y' for yes or 'n' for no.")

    if choice == 'n':
        break

# Show the order receipt when the customer has finished ordering
if choice == 'n':
    print("\nOrder Receipt")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")

    # Loop through the customer order list 
    for item in order:
        # Saving the values of each key as their own variable for item name, price & quantity
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # Calculate the number of empty spaces for formatting for the order receipt
        spaces_item_name = " " * (26 - len(item_name))
        spaces_price = " " * (7 - len(str(price)))
        
        # Print the line for the customer receipt using the specified format from line 89
        print(f"{item_name}{spaces_item_name}| ${price:.2f}{spaces_price}| {quantity}")

    # Calculate and display the total price of the customer order along with all the items they ordered
    total_price = sum(item["Price"] * item["Quantity"] for item in order)
    print(f"\nTotal Price: ${total_price:.2f}")