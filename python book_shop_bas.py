import datetime

class BookShop:
    def __init__(self):
        """
        Initialize the book shop with an empty inventory, sales records, and requests.
        """
        self.inventory = {}  # Inventory to hold book details
        self.sales = []  # List to hold sales transactions
        self.requests = {}  # Requests for books not in stock
        self.stockists = {}  # Vendor details for each publisher
        self.transaction_count = 0  # Serial number for transactions

    def add_book(self):
        """
        Add a new book or restock an existing book.
        """
        isbn = input("Enter ISBN number: ").strip()
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        publisher = input("Enter publisher name: ").strip()
        price = float(input("Enter book price: "))
        quantity = int(input("Enter quantity: "))
        rack_number = input("Enter rack number: ").strip()

        if isbn in self.inventory:
            # Update existing book
            self.inventory[isbn]['quantity'] += quantity
            print(f"Book '{title}' updated with {quantity} additional copies.\n")
        else:
            # Add new book
            self.inventory[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'price': price,
                'quantity': quantity,
                'rack_number': rack_number
            }
            print(f"Book '{title}' added to the inventory.\n")

        # Store the stockist information
        if publisher not in self.stockists:
            stockist_name = input("Enter stockist name: ").strip()
            stockist_address = input("Enter stockist address: ").strip()
            self.stockists[publisher] = {
                'name': stockist_name,
                'address': stockist_address
            }

    def check_availability(self):
        """
        Check if a book is available by title or author.
        """
        query = input("Enter book title or author to search: ").strip()
        found_books = []

        # Search by title or author
        for isbn, book in self.inventory.items():
            if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
                found_books.append(book)

        if found_books:
            print(f"\n{'Title':<20} {'Author':<20} {'Quantity':<10} {'Rack Number':<15}")
            print("-" * 65)
            for book in found_books:
                print(f"{book['title']:<20} {book['author']:<20} {book['quantity']:<10} {book['rack_number']:<15}")
        else:
            print("Book not found in stock. You can request this book for future procurement.")
            self.handle_request(query)

    def handle_request(self, query):
        """
        Handle requests for books not in stock by incrementing the request counter.
        """
        if query in self.requests:
            self.requests[query] += 1
        else:
            self.requests[query] = 1
        print(f"Request for '{query}' has been recorded.\n")

    def sell_book(self):
        """
        Process a book sale and generate a sales receipt.
        """
        print("\n--- Book Sale Transaction ---")
        isbn = input("Enter ISBN number of the book: ").strip()

        if isbn not in self.inventory:
            print("Book not found in inventory.\n")
            return

        book = self.inventory[isbn]
        quantity = int(input(f"Enter quantity of '{book['title']}' to purchase: "))

        if quantity > book['quantity']:
            print(f"Insufficient stock. Available: {book['quantity']} copies.\n")
            return

        # Update inventory
        book['quantity'] -= quantity
        total_price = book['price'] * quantity

        # Generate the sales receipt
        self.transaction_count += 1
        self.sales.append({
            'transaction_id': self.transaction_count,
            'isbn': isbn,
            'title': book['title'],
            'quantity': quantity,
            'unit_price': book['price'],
            'total_price': total_price,
            'date': datetime.date.today()
        })

        print("\n--- Sales Receipt ---")
        print(f"Transaction ID: {self.transaction_count}")
        print(f"Book: {book['title']}")
        print(f"Quantity: {quantity}")
        print(f"Unit Price: ${book['price']:.2f}")
        print(f"Total Price: ${total_price:.2f}")
        print("Thank you for your purchase!\n")

    def update_inventory(self):
        """
        Update the inventory when new stock arrives.
        """
        isbn = input("Enter ISBN number for restocking: ").strip()
        if isbn in self.inventory:
            quantity = int(input("Enter quantity to restock: "))
            self.inventory[isbn]['quantity'] += quantity
            print(f"Book '{self.inventory[isbn]['title']}' restocked with {quantity} copies.\n")
        else:
            print("Book not found in inventory.\n")

    def sales_statistics(self):
        """
        Generate sales statistics for a given date range.
        """
        start_date_input = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date_input = input("Enter end date (YYYY-MM-DD): ").strip()

        try:
            start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please try again.\n")
            return

        print("\n--- Sales Statistics ---")
        print(f"{'Transaction ID':<15} {'Date':<12} {'Title':<30} {'Quantity':<10} {'Revenue':<10}")
        print("-" * 80)

        total_revenue = 0
        for sale in self.sales:
            if start_date <= sale['date'] <= end_date:
                print(f"{sale['transaction_id']:<15} {sale['date']} {sale['title']:<30} {sale['quantity']:<10} ${sale['total_price']:.2f}")
                total_revenue += sale['total_price']

        print("-" * 80)
        print(f"Total Revenue from {start_date} to {end_date}: ${total_revenue:.2f}\n")

    def check_inventory_threshold(self):
        """
        Print books that have fallen below the threshold and their stockist details.
        """
        print("\n--- Inventory Threshold Check ---")
        threshold = int(input("Enter threshold quantity: "))

        for isbn, book in self.inventory.items():
            if book['quantity'] < threshold:
                stockist_info = self.stockists.get(book['publisher'])
                print(f"Book: {book['title']} | Quantity: {book['quantity']} | Threshold: {threshold}")
                if stockist_info:
                    print(f"Stockist: {stockist_info['name']} | Address: {stockist_info['address']}\n")


def main():
    book_shop = BookShop()

    while True:
        print("\n--- Book-shop Automation Software (BAS) ---")
        print("1. Add/Restock Book")
        print("2. Check Book Availability")
        print("3. Sell Book")
        print("4. Update Inventory")
        print("5. View Sales Statistics")
        print("6. Check Inventory Threshold")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            book_shop.add_book()
        elif choice == "2":
            book_shop.check_availability()
        elif choice == "3":
            book_shop.sell_book()
        elif choice == "4":
            book_shop.update_inventory()
        elif choice == "5":
            book_shop.sales_statistics()
        elif choice == "6":
            book_shop.check_inventory_threshold()
        elif choice == "7":
            print("Exiting... Thank you for using BAS!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
