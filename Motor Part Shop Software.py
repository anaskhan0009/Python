class MotorPartShopSoftware:
    def __init__(self):
        self.parts = {}  # stores part information
        self.sales = {}  # keeps track of sales for parts
        self.revenue = 0  # total daily revenue
        self.monthly_sales = {}  # stores monthly sales by part
        self.vendors = {}  # stores vendor info for each part

    def add_part(self):
        """Add a new motor part to inventory."""
        part_number = input("Enter part number: ")
        part_name = input("Enter part name: ")
        vendor_name = input("Enter vendor name: ")
        vendor_address = input("Enter vendor address: ")
        price = float(input("Enter price per part: "))
        threshold_sales_per_week = int(input("Enter threshold sales per week: "))

        self.parts[part_number] = {
            'name': part_name,
            'vendor_name': vendor_name,
            'vendor_address': vendor_address,
            'price': price,
            'threshold_sales_per_week': threshold_sales_per_week,
            'inventory': 0
        }
        self.vendors[part_number] = vendor_address
        print(f"Part {part_name} added to inventory.")

    def update_inventory(self):
        """Update the inventory for a given part."""
        part_number = input("Enter part number to update inventory: ")
        if part_number in self.parts:
            quantity = int(input("Enter quantity to add to inventory: "))
            self.parts[part_number]['inventory'] += quantity
            print(f"Inventory for {self.parts[part_number]['name']} updated. New quantity: {self.parts[part_number]['inventory']}.")
        else:
            print("Part not found.")

    def record_sale(self):
        """Record a sale of a part."""
        part_number = input("Enter part number to record sale: ")
        if part_number in self.parts:
            quantity_sold = int(input(f"Enter quantity sold for {self.parts[part_number]['name']}: "))
            if self.parts[part_number]['inventory'] >= quantity_sold:
                self.parts[part_number]['inventory'] -= quantity_sold
                self.sales[part_number] = self.sales.get(part_number, 0) + quantity_sold
                self.revenue += self.parts[part_number]['price'] * quantity_sold
                if part_number in self.monthly_sales:
                    self.monthly_sales[part_number] += quantity_sold
                else:
                    self.monthly_sales[part_number] = quantity_sold
                print(f"Sale recorded: {quantity_sold} of {self.parts[part_number]['name']}.")
            else:
                print("Not enough stock to complete the sale.")
        else:
            print("Part not found.")

    def generate_order_report(self):
        """Generate order report for parts that need to be reordered."""
        print("\n--- Parts to be Ordered ---")
        for part_number, part in self.parts.items():
            avg_sales_per_week = self.sales.get(part_number, 0) // 7
            threshold_inventory = part['threshold_sales_per_week']
            if part['inventory'] < threshold_inventory:
                amount_to_order = threshold_inventory - part['inventory']
                print(f"Part: {part['name']}, Vendor: {part['vendor_name']}, Address: {part['vendor_address']}, Amount to Order: {amount_to_order}")

    def generate_daily_revenue(self):
        """Print the daily revenue report."""
        print(f"\nTotal Daily Revenue: ${self.revenue:.2f}")

    def generate_monthly_sales_report(self):
        """Generate a monthly sales report showing sales per part."""
        print("\n--- Monthly Sales Report ---")
        for part_number, sales in self.monthly_sales.items():
            part_name = self.parts[part_number]['name']
            print(f"Part: {part_name}, Sales: {sales}, Revenue: ${self.parts[part_number]['price'] * sales:.2f}")

    def query_inventory(self):
        """Display current inventory of all parts."""
        print("\n--- Current Inventory ---")
        for part_number, part in self.parts.items():
            print(f"Part: {part['name']}, Inventory: {part['inventory']}")


# Main function to demonstrate the system
def main():
    # Instantiate the shop software
    shop = MotorPartShopSoftware()

    while True:
        print("\nMotor Part Shop Software")
        print("1. Add Part")
        print("2. Update Inventory")
        print("3. Record Sale")
        print("4. Generate Order Report")
        print("5. Generate Daily Revenue")
        print("6. Generate Monthly Sales Report")
        print("7. Query Inventory")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            shop.add_part()
        elif choice == '2':
            shop.update_inventory()
        elif choice == '3':
            shop.record_sale()
        elif choice == '4':
            shop.generate_order_report()
        elif choice == '5':
            shop.generate_daily_revenue()
        elif choice == '6':
            shop.generate_monthly_sales_report()
        elif choice == '7':
            shop.query_inventory()
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
