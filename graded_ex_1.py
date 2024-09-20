# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        total_cost = 0
        for item in cart:
            product, price, quantity = item
            print(f"{product} - ${price} x {quantity} = ${price * quantity}")
            total_cost += price * quantity
        print(f"Total cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, address):
    print(f"Receipt for {name} <{email}>")
    print("Products:")
    total_cost = 0
    for item in cart:
        product, price, quantity = item
        print(f"{product} - ${price} x {quantity}")
        total_cost += price * quantity
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")

def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=sort_order == 'desc')
    display_products(sorted_products)
    return sorted_products

def main():
    cart = []
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name (First Name Last Name).")
        name = input("Please enter your name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email address.")
        email = input("Please enter your email address: ")

    display_categories()
    while True:
        category_choice = input("Which category would you like to explore? ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(products):
            selected_category = list(products.keys())[int(category_choice) - 1]
            products_list = products[selected_category]
            display_products(products_list)

            while True:
                print("\n1. Select a product to buy")
                print("2. Sort the products according to the price.")
                print("3. Go back to the category selection.")
                print("4. Finish shopping")
                choice = input("Please enter your choice: ")

                if choice == '1':
                    product_choice = input("Enter the number of the product you want to buy: ")
                    if product_choice.isdigit() and 1 <= int(product_choice) <= len(products_list):
                        product, price = products_list[int(product_choice) - 1]
                        quantity = int(input("Enter the quantity you want to buy: "))
                        add_to_cart(cart, (product, price), quantity)
                    else:
                        print("Invalid product choice. Please try again.")

                elif choice == '2':
                    sort_order = input("Sort by 1 for ascending or 2 for descending: ")
                    sorted_products = display_sorted_products(products_list, 'asc' if sort_order == '1' else 'desc')

                elif choice == '3':
                    display_categories()
                    break

                elif choice == '4':
                    if cart:
                        address = input("Please enter your delivery address: ")
                        generate_receipt(name, email, cart, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    break

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid category choice. Please try again.")

if __name__ == "__main__":
    main()