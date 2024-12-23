import datetime

# Initialize data
menu = {
    "101": {"name": "Burger", "price": 50},
    "102": {"name": "Pizza", "price": 150},
    "103": {"name": "Pasta", "price": 120},
    "104": {"name": "Sandwich", "price": 60},
    "105": {"name": "Coffee", "price": 40},
}

inventory = {
    "Bread": {"stock": 10, "threshold": 4, "consumption": [0, 0, 0]},
    "Cheese": {"stock": 5, "threshold": 2, "consumption": [0, 0, 0]},
    "Coffee Beans": {"stock": 8, "threshold": 3, "consumption": [0, 0, 0]},
}

cash_balance = 1000
daily_sales = []
expenses = []


def display_menu():
    print("\n------ Menu ------")
    for code, details in menu.items():
        print(f"Code: {code} | Item: {details['name']} | Price: Rs. {details['price']}")
    print("------------------")


def update_prices():
    print("\n--- Update Menu Prices ---")
    for code, details in menu.items():
        print(f"Current price of {details['name']}: Rs. {details['price']}")
        new_price = input(f"Enter new price for {details['name']} (or press Enter to skip): ").strip()
        if new_price.isdigit():
            menu[code]['price'] = int(new_price)
            print(f"Price updated for {details['name']}.")
    print("All updates completed.")


def take_order():
    global cash_balance
    print("\n--- Take Customer Order ---")
    display_menu()
    order = {}
    total_amount = 0

    while True:
        code = input("Enter item code (or 'done' to finish): ").strip()
        if code.lower() == 'done':
            break
        if code not in menu:
            print("Invalid item code! Please try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {menu[code]['name']}: ").strip())
            if quantity > 0:
                order[code] = order.get(code, 0) + quantity
                total_amount += menu[code]['price'] * quantity
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number for quantity.")

    if order:
        print("\n------ Bill ------")
        for code, qty in order.items():
            print(f"{menu[code]['name']} x {qty} = Rs. {menu[code]['price'] * qty}")
        print(f"Total Amount: Rs. {total_amount}")
        print("------------------")
        cash_balance += total_amount
        daily_sales.append({"date": datetime.date.today(), "order": order, "total": total_amount})
        print("Order completed successfully!")
    else:
        print("No items ordered.")


def update_inventory():
    print("\n--- Update Inventory Consumption ---")
    for item, details in inventory.items():
        try:
            consumed = int(input(f"Enter quantity consumed for {item} today: ").strip())
            details['consumption'].pop(0)
            details['consumption'].append(consumed)
            details['stock'] -= consumed
            if details['stock'] < 0:
                print(f"Warning: {item} is out of stock!")
            print(f"Updated stock of {item}: {details['stock']} units.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def generate_purchase_orders():
    print("\n--- Generate Purchase Orders ---")
    for item, details in inventory.items():
        avg_consumption = sum(details['consumption']) // 3
        threshold = avg_consumption * 2  # Two days' worth of stock
        inventory[item]['threshold'] = threshold

        if details['stock'] < threshold:
            quantity_needed = threshold * 2 - details['stock']
            print(f"Order {quantity_needed} units of {item} (Current Stock: {details['stock']}, Threshold: {threshold}).")


def record_expenses():
    global cash_balance
    print("\n--- Record Expenses ---")
    expense_item = input("Enter expense description: ").strip()
    try:
        amount = int(input("Enter amount: ").strip())
        if cash_balance >= amount:
            cash_balance -= amount
            expenses.append({"description": expense_item, "amount": amount, "date": datetime.date.today()})
            print(f"Expense recorded. Remaining cash balance: Rs. {cash_balance}")
        else:
            print("Insufficient cash balance to record this expense.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


def show_monthly_report():
    print("\n--- Monthly Sales and Expense Report ---")
    total_sales = sum(order['total'] for order in daily_sales)
    total_expenses = sum(exp['amount'] for exp in expenses)
    print(f"Total Sales: Rs. {total_sales}")
    print(f"Total Expenses: Rs. {total_expenses}")
    print(f"Net Balance: Rs. {cash_balance}")


def main():
    while True:
        print("\n--- Restaurant Automation System ---")
        print("1. Display Menu")
        print("2. Update Menu Prices")
        print("3. Take Order and Generate Bill")
        print("4. Update Inventory Consumption")
        print("5. Generate Purchase Orders")
        print("6. Record Expenses")
        print("7. Show Monthly Sales and Expense Report")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_menu()
        elif choice == '2':
            update_prices()
        elif choice == '3':
            take_order()
        elif choice == '4':
            update_inventory()
        elif choice == '5':
            generate_purchase_orders()
        elif choice == '6':
            record_expenses()
        elif choice == '7':
            show_monthly_report()
        elif choice == '8':
            print("Exiting... Thank you for using the Restaurant Automation System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
