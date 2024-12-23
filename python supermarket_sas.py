import datetime

class Supermarket:
    def __init__(self):
        """
        Initialize the supermarket with an empty inventory and sales records.
        """
        self.inventory = {}  # Inventory to hold item details
        self.sales = []  # List to hold sales transactions
        self.transaction_count = 0  # Serial number for transactions

    def add_item(self):
        """
        Add a new item or restock an existing item in the inventory.
        """
        item_code = input("Enter item code: ").strip()
        name = input("Enter item name: ").strip()
        quantity = int(input("Enter quantity: "))
        unit_price = float(input("Enter unit price: "))
        cost_price = float(input("Enter cost price: "))

        if item_code in self.inventory:
            # Update existing item
            self.inventory[item_code]['quantity'] += quantity
            print(f"Item '{name}' updated with {quantity} additional units.\n")
        else:
            # Add new item
            self.inventory[item_code] = {
                'name': name,
                'quantity': quantity,
                'unit_price': unit_price,
                'cost_price': cost_price
            }
            print(f"Item '{name}' added to the inventory.\n")

    def update_item_price(self):
        """
        Update the selling price of an existing item.
        """
        item_code = input("Enter item code to update price: ").strip()
        if item_code in self.inventory:
            new_price = float(input("Enter new unit price: "))
            self.inventory[item_code]['unit_price'] = new_price
            print(f"Price updated for item '{self.inventory[item_code]['name']}' to {new_price}.\n")
        else:
            print("Item not found in inventory.\n")

    def sell_item(self):
        """
        Process a sales transaction.
        """
        print("\n--- Sales Transaction ---")
        transaction = []
        total_amount = 0.0

        while True:
            item_code = input("Enter item code (or 'done' to finish): ").strip()
            if item_code.lower() == 'done':
                break

            if item_code not in self.inventory:
                print("Item not found in inventory. Try again.")
                continue

            quantity = int(input("Enter quantity: "))
            item = self.inventory[item_code]

            if quantity > item['quantity']:
                print(f"Insufficient stock. Available: {item['quantity']}")
                continue

            # Update inventory
            item['quantity'] -= quantity

            # Calculate item price
            item_price = quantity * item['unit_price']
            total_amount += item_price

            # Record item in transaction
            transaction.append({
                'code': item_code,
                'name': item['name'],
                'quantity': quantity,
                'unit_price': item['unit_price'],
                'item_price': item_price
            })

            print(f"Item '{item['name']}' added to the bill.\n")

        if transaction:
            self.transaction_count += 1
            self.sales.append({'transaction_id': self.transaction_count,
                               'date': datetime.date.today(),
                               'items': transaction,
                               'total_amount': total_amount})
            self.print_bill(transaction, total_amount)

    def print_bill(self, transaction, total_amount):
        """
        Print the bill for a sales transaction.
        """
        print("\n--- Supermarket Bill ---")
        print(f"Transaction ID: {self.transaction_count}")
        print(f"{'Item':<15} {'Code':<10} {'Qty':<5} {'Unit Price':<10} {'Item Price':<10}")
        print("-" * 60)

        for item in transaction:
            print(f"{item['name']:<15} {item['code']:<10} {item['quantity']:<5} {item['unit_price']:<10.2f} {item['item_price']:<10.2f}")

        print("-" * 60)
        print(f"Total Amount Payable: ${total_amount:.2f}")
        print("Thank you for shopping!\n")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        print("\n--- Inventory Details ---")
        if not self.inventory:
            print("No items in inventory.\n")
            return

        print(f"{'Code':<10} {'Name':<15} {'Qty':<10} {'Unit Price':<10} {'Cost Price':<10}")
        print("-" * 55)

        for code, details in self.inventory.items():
            print(f"{code:<10} {details['name']:<15} {details['quantity']:<10} {details['unit_price']:<10.2f} {details['cost_price']:<10.2f}")
        print()

    def sales_statistics(self):
        """
        Print sales statistics for a given date.
        """
        date_input = input("Enter date (YYYY-MM-DD) for sales statistics: ").strip()
        try:
            query_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Try again.\n")
            return

        total_sales = 0.0
        print("\n--- Sales Statistics ---")
        print(f"{'Transaction ID':<15} {'Date':<12} {'Amount':<10}")
        print("-" * 40)

        for sale in self.sales:
            if sale['date'] == query_date:
                print(f"{sale['transaction_id']:<15} {sale['date']} ${sale['total_amount']:.2f}")
                total_sales += sale['total_amount']

        print("-" * 40)
        print(f"Total Sales for {query_date}: ${total_sales:.2f}\n")


def main():
    supermarket = Supermarket()

    while True:
        print("\n--- Supermarket Automation Software (SAS) ---")
        print("1. Add/Restock Item")
        print("2. Update Item Price")
        print("3. Sell Items")
        print("4. View Inventory")
        print("5. View Sales Statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            supermarket.add_item()
        elif choice == "2":
            supermarket.update_item_price()
        elif choice == "3":
            supermarket.sell_item()
        elif choice == "4":
            supermarket.view_inventory()
        elif choice == "5":
            supermarket.sales_statistics()
        elif choice == "6":
            print("Exiting... Thank you for using SAS!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
