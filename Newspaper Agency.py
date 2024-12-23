from datetime import datetime, timedelta

class NewspaperAgency:
    def __init__(self):
        self.customers = {}
        self.delivery_persons = {}
        self.publications = ["Newspaper", "Magazine"]
        self.delivery_schedule = {}  # Stores delivery schedule for each delivery person
        self.payment_due = {}  # Tracks overdue payments for customers

    def add_customer(self, customer_id, name, subscription, address):
        """Add a new customer with subscription details."""
        self.customers[customer_id] = {
            "name": name,
            "subscription": subscription,  # List of subscribed publications
            "address": address,
            "outstanding_due": 0.0,  # Customer's outstanding payment
            "last_payment_date": None,  # Last payment made by the customer
        }
        print(f"Customer {name} added successfully!")

    def modify_subscription(self, customer_id, new_subscription):
        """Modify subscription list for a customer."""
        if customer_id in self.customers:
            self.customers[customer_id]["subscription"] = new_subscription
            print(f"Subscription for customer {customer_id} modified.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def stop_subscription(self, customer_id):
        """Stop the subscription for a customer."""
        if customer_id in self.customers:
            self.customers[customer_id]["subscription"] = []
            print(f"Subscription for customer {customer_id} stopped.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def add_delivery_person(self, delivery_id, name):
        """Add a delivery person to the system."""
        self.delivery_persons[delivery_id] = {"name": name, "commission": 0.0}
        print(f"Delivery person {name} added.")

    def assign_delivery(self, delivery_id, customer_id):
        """Assign a delivery to a delivery person."""
        if delivery_id not in self.delivery_schedule:
            self.delivery_schedule[delivery_id] = []
        if customer_id in self.customers:
            self.delivery_schedule[delivery_id].append(customer_id)
            print(f"Assigned customer {customer_id} to delivery person {delivery_id}.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def generate_daily_delivery(self, delivery_id):
        """Print daily deliveries for a delivery person."""
        if delivery_id in self.delivery_schedule:
            print(f"\nDelivery list for {self.delivery_persons[delivery_id]['name']}:")
            for customer_id in self.delivery_schedule[delivery_id]:
                customer = self.customers[customer_id]
                print(f"Customer {customer['name']} at {customer['address']} will receive {', '.join(customer['subscription'])}")
        else:
            print(f"Delivery person with ID {delivery_id} not found.")

    def generate_monthly_bills(self):
        """Generate bills for all customers at the start of each month."""
        current_month = datetime.now().month
        print(f"\nMonthly Bills for {datetime.now().strftime('%B')}:")

        for customer_id, customer in self.customers.items():
            bill = 0.0
            for pub in customer["subscription"]:
                bill += 5.0  # Assume cost of each publication is 5 units
            customer["outstanding_due"] += bill
            print(f"Customer {customer['name']}: {bill} units due.")
    
    def process_payment(self, customer_id, amount_paid):
        """Process the payment from a customer."""
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            customer["outstanding_due"] -= amount_paid
            customer["last_payment_date"] = datetime.now()
            print(f"Payment of {amount_paid} units received from {customer['name']}.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def overdue_payments(self):
        """Generate a list of customers with overdue payments."""
        print("\nCustomers with Overdue Payments:")
        for customer_id, customer in self.customers.items():
            if customer["outstanding_due"] > 0:
                last_payment = customer["last_payment_date"]
                if last_payment and (datetime.now() - last_payment).days > 30:
                    print(f"Customer {customer['name']}, Outstanding: {customer['outstanding_due']} units")

    def print_receipt(self, customer_id, amount_paid):
        """Print receipt for a customer after payment."""
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            print(f"\nReceipt for {customer['name']}:")
            print(f"Amount Paid: {amount_paid} units")
            print(f"Remaining Balance: {customer['outstanding_due']} units")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def calculate_delivery_person_commission(self):
        """Calculate commission for delivery persons based on the value of the publications delivered."""
        for delivery_id, deliveries in self.delivery_schedule.items():
            total_value = 0
            for customer_id in deliveries:
                customer = self.customers[customer_id]
                for publication in customer["subscription"]:
                    total_value += 5.0  # Assuming each publication costs 5 units
            commission = total_value * 0.025  # 2.5% commission
            self.delivery_persons[delivery_id]["commission"] = commission
            print(f"Delivery person {self.delivery_persons[delivery_id]['name']} will receive a commission of {commission} units.")

    def generate_summary(self):
        """Generate a summary for the current month."""
        print("\nMonthly Summary:")
        self.generate_monthly_bills()
        self.overdue_payments()
        self.calculate_delivery_person_commission()

def print_menu():
    """Display the menu options for the manager."""
    print("\n--- Newspaper Agency Automation Software ---")
    print("1. Add Customer")
    print("2. Modify Customer Subscription")
    print("3. Stop Customer Subscription")
    print("4. Add Delivery Person")
    print("5. Assign Delivery to Delivery Person")
    print("6. Generate Daily Delivery List")
    print("7. Generate Monthly Bills")
    print("8. Process Payment")
    print("9. Generate Receipt")
    print("10. Overdue Payments Report")
    print("11. Generate Monthly Summary")
    print("0. Exit")

def main():
    """Main function to interact with the user."""
    agency = NewspaperAgency()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            subscription = input("Enter subscriptions (comma separated): ").split(",")
            address = input("Enter customer address: ")
            agency.add_customer(customer_id, name, subscription, address)

        elif choice == '2':
            customer_id = int(input("Enter customer ID to modify subscription: "))
            new_subscription = input("Enter new subscriptions (comma separated): ").split(",")
            agency.modify_subscription(customer_id, new_subscription)

        elif choice == '3':
            customer_id = int(input("Enter customer ID to stop subscription: "))
            agency.stop_subscription(customer_id)

        elif choice == '4':
            delivery_id = int(input("Enter delivery person ID: "))
            name = input("Enter delivery person name: ")
            agency.add_delivery_person(delivery_id, name)

        elif choice == '5':
            delivery_id = int(input("Enter delivery person ID: "))
            customer_id = int(input("Enter customer ID to assign delivery: "))
            agency.assign_delivery(delivery_id, customer_id)

        elif choice == '6':
            delivery_id = int(input("Enter delivery person ID: "))
            agency.generate_daily_delivery(delivery_id)

        elif choice == '7':
            agency.generate_monthly_bills()

        elif choice == '8':
            customer_id = int(input("Enter customer ID for payment: "))
            amount_paid = float(input("Enter amount paid: "))
            agency.process_payment(customer_id, amount_paid)

        elif choice == '9':
            customer_id = int(input("Enter customer ID for receipt: "))
            amount_paid = float(input("Enter amount paid: "))
            agency.print_receipt(customer_id, amount_paid)

        elif choice == '10':
            agency.overdue_payments()

        elif choice == '11':
            agency.generate_summary()

        elif choice == '0':
            print("Exiting Newspaper Agency Automation Software.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
