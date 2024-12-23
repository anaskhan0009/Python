import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class LibraryInformationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Information System")
        self.root.geometry("900x600")
        self.root.config(bg="#2F1E1E")  # Red-themed background

        # Title Label
        self.title_label = tk.Label(
            self.root, 
            text="Library Information System", 
            font=("Helvetica", 26, "bold"), 
            bg="#2F1E1E", 
            fg="#FF4C4C"  # Bright red for the title
        )
        self.title_label.pack(pady=20)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=20)

        # Tabs
        self.add_book_tab = tk.Frame(self.notebook, bg="#401E1E")
        self.issue_book_tab = tk.Frame(self.notebook, bg="#401E1E")
        self.return_book_tab = tk.Frame(self.notebook, bg="#401E1E")
        self.query_tab = tk.Frame(self.notebook, bg="#401E1E")

        self.notebook.add(self.add_book_tab, text="Add Book")
        self.notebook.add(self.issue_book_tab, text="Issue Book")
        self.notebook.add(self.return_book_tab, text="Return Book")
        self.notebook.add(self.query_tab, text="Query Book")

        # Tab Widgets
        self.add_book_tab_widgets()
        self.issue_book_tab_widgets()
        self.return_book_tab_widgets()
        self.query_book_tab_widgets()

        # Data Structures
        self.books = {}  # ISBN -> {"title": ..., "rack": ..., "copies": ...}

        # Load existing data from file
        self.load_data()

    def styled_button(self, parent, text, command):
        return tk.Button(
            parent, 
            text=text, 
            command=command, 
            bg="#FF4C4C",  # Red button background
            fg="white", 
            font=("Arial", 14, "bold"), 
            activebackground="#E63939",  # Darker red on click
            relief="raised", 
            bd=2
        )

    def add_book_tab_widgets(self):
        tk.Label(
            self.add_book_tab, 
            text="Add New Book", 
            font=("Helvetica", 20, "bold"), 
            bg="#401E1E", 
            fg="#FF4C4C"
        ).pack(pady=10)

        form_frame = tk.Frame(self.add_book_tab, bg="#401E1E")
        form_frame.pack(pady=20)

        labels = ["ISBN:", "Title:", "Rack Number:", "Copies:"]
        self.add_book_entries = {}

        for i, label_text in enumerate(labels):
            tk.Label(
                form_frame, 
                text=label_text, 
                font=("Arial", 14), 
                bg="#401E1E", 
                fg="white"
            ).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            entry = tk.Entry(form_frame, font=("Arial", 14))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.add_book_entries[label_text[:-1].lower()] = entry

        self.styled_button(self.add_book_tab, "Add Book", self.add_book).pack(pady=10)

    def issue_book_tab_widgets(self):
        tk.Label(
            self.issue_book_tab, 
            text="Issue Book", 
            font=("Helvetica", 20, "bold"), 
            bg="#401E1E", 
            fg="#FF4C4C"
        ).pack(pady=10)

        form_frame = tk.Frame(self.issue_book_tab, bg="#401E1E")
        form_frame.pack(pady=20)

        labels = ["Member ID:", "ISBN:"]
        self.issue_book_entries = {}

        for i, label_text in enumerate(labels):
            tk.Label(
                form_frame, 
                text=label_text, 
                font=("Arial", 14), 
                bg="#401E1E", 
                fg="white"
            ).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            entry = tk.Entry(form_frame, font=("Arial", 14))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.issue_book_entries[label_text[:-1].lower()] = entry

        self.styled_button(self.issue_book_tab, "Issue Book", self.issue_book).pack(pady=10)

    def return_book_tab_widgets(self):
        tk.Label(
            self.return_book_tab, 
            text="Return Book", 
            font=("Helvetica", 20, "bold"), 
            bg="#401E1E", 
            fg="#FF4C4C"
        ).pack(pady=10)

        form_frame = tk.Frame(self.return_book_tab, bg="#401E1E")
        form_frame.pack(pady=20)

        labels = ["Member ID:", "ISBN:"]
        self.return_book_entries = {}

        for i, label_text in enumerate(labels):
            tk.Label(
                form_frame, 
                text=label_text, 
                font=("Arial", 14), 
                bg="#401E1E", 
                fg="white"
            ).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            entry = tk.Entry(form_frame, font=("Arial", 14))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.return_book_entries[label_text[:-1].lower()] = entry

        self.styled_button(self.return_book_tab, "Return Book", self.return_book).pack(pady=10)

    def query_book_tab_widgets(self):
        tk.Label(
            self.query_tab, 
            text="Query Book", 
            font=("Helvetica", 20, "bold"), 
            bg="#401E1E", 
            fg="#FF4C4C"
        ).pack(pady=10)

        form_frame = tk.Frame(self.query_tab, bg="#401E1E")
        form_frame.pack(pady=20)

        tk.Label(
            form_frame, 
            text="ISBN:", 
            font=("Arial", 14), 
            bg="#401E1E", 
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.query_isbn_entry = tk.Entry(form_frame, font=("Arial", 14))
        self.query_isbn_entry.grid(row=0, column=1, padx=10, pady=5)

        self.styled_button(self.query_tab, "Check Availability", self.query_book).pack(pady=10)

    # Core Functionality
    def add_book(self):
        isbn = self.add_book_entries["isbn"].get()
        title = self.add_book_entries["title"].get()
        rack = self.add_book_entries["rack number"].get()
        copies = self.add_book_entries["copies"].get()

        if not isbn or not title or not rack or not copies.isdigit():
            messagebox.showerror("Error", "All fields must be filled correctly.")
            return
        
        self.books[isbn] = {"title": title, "rack": rack, "copies": int(copies)}
        self.save_data()  # Save data to file
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")
        
        for entry in self.add_book_entries.values():
            entry.delete(0, tk.END)

    def issue_book(self):
        member_id = self.issue_book_entries["member id"].get().strip()
        isbn = self.issue_book_entries["isbn"].get().strip()

        if not member_id or not isbn:
            messagebox.showerror("Error", "Both Member ID and ISBN are required.")
            return

        book = self.books.get(isbn)

        if book and book["copies"] > 0:
            book["copies"] -= 1
            self.save_data()  # Save data to file
            messagebox.showinfo("Success", f"Book '{book['title']}' issued successfully!")
        else:
            messagebox.showerror("Error", "Book not available for issue.")

        for entry in self.issue_book_entries.values():
            entry.delete(0, tk.END)

    def return_book(self):
        member_id = self.return_book_entries["member id"].get().strip()
        isbn = self.return_book_entries["isbn"].get().strip()

        if not member_id or not isbn:
            messagebox.showerror("Error", "Both Member ID and ISBN are required.")
            return

        book = self.books.get(isbn)

        if book:
            book["copies"] += 1
            self.save_data()  # Save data to file
            messagebox.showinfo("Success", f"Book '{book['title']}' returned successfully!")
        else:
            messagebox.showerror("Error", "Book not found in the library.")

        for entry in self.return_book_entries.values():
            entry.delete(0, tk.END)

    def query_book(self):
        isbn = self.query_isbn_entry.get().strip()

        if not isbn:
            messagebox.showerror("Error", "ISBN is required.")
            return

        book = self.books.get(isbn)

        if book:
            messagebox.showinfo(
                "Book Information",
                f"Title: {book['title']}\nRack: {book['rack']}\nCopies Available: {book['copies']}"
            )
        else:
            messagebox.showerror("Error", "Book not found in the library.")

        self.query_isbn_entry.delete(0, tk.END)

    # File Handling
    def save_data(self):
        with open("library_data.json", "w") as f:
            json.dump(self.books, f, indent=4)

    def load_data(self):
        try:
            with open("library_data.json", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = {}

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryInformationSystem(root)
    root.mainloop()
