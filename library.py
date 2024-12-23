import tkinter as tk
from tkinter import messagebox, ttk
import json
import bcrypt
import os

# JSON file for storing data
DB_FILE = "library_gui.json"


# Initialize the JSON file if it doesn't exist
def initialize_db():
    if not os.path.exists(DB_FILE):
        data = {
            "users": [],
            "books": [],
        }
        with open(DB_FILE, "w") as file:
            json.dump(data, file, indent=4)


# Load data from the JSON file
def load_data():
    with open(DB_FILE, "r") as file:
        return json.load(file)


# Save data to the JSON file
def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


# GUI Functionality
class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")

        self.current_user = None

        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.show_login_page()

    # Login Page
    def show_login_page(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Email:").pack()
        self.login_email_entry = tk.Entry(self.main_frame)
        self.login_email_entry.pack()

        tk.Label(self.main_frame, text="Password:").pack()
        self.login_password_entry = tk.Entry(self.main_frame, show="*")
        self.login_password_entry.pack()

        tk.Button(self.main_frame, text="Login", command=self.login_user).pack(pady=5)
        tk.Button(self.main_frame, text="Register", command=self.show_register_page).pack()

    # Registration Page
    def show_register_page(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Register", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="User Type (Student/Professor):").pack()
        self.register_type_entry = tk.Entry(self.main_frame)
        self.register_type_entry.pack()

        tk.Label(self.main_frame, text="UID:").pack()
        self.register_uid_entry = tk.Entry(self.main_frame)
        self.register_uid_entry.pack()

        tk.Label(self.main_frame, text="Name:").pack()
        self.register_name_entry = tk.Entry(self.main_frame)
        self.register_name_entry.pack()

        tk.Label(self.main_frame, text="Department:").pack()
        self.register_department_entry = tk.Entry(self.main_frame)
        self.register_department_entry.pack()

        tk.Label(self.main_frame, text="Email:").pack()
        self.register_email_entry = tk.Entry(self.main_frame)
        self.register_email_entry.pack()

        tk.Label(self.main_frame, text="Phone Number:").pack()
        self.register_phone_entry = tk.Entry(self.main_frame)
        self.register_phone_entry.pack()

        tk.Label(self.main_frame, text="Password:").pack()
        self.register_password_entry = tk.Entry(self.main_frame, show="*")
        self.register_password_entry.pack()

        tk.Button(self.main_frame, text="Register", command=self.register_user).pack(pady=5)
        tk.Button(self.main_frame, text="Back to Login", command=self.show_login_page).pack()

    # User Dashboard
    def show_dashboard(self):
        self.clear_frame()

        tk.Label(self.main_frame, text=f"Welcome, {self.current_user['name']}", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="View Books", command=self.view_books).pack(pady=5)
        tk.Button(self.main_frame, text="Add Book (Admin Only)", command=self.add_book_page).pack(pady=5)
        tk.Button(self.main_frame, text="Logout", command=self.logout).pack(pady=5)

    # Book Viewing Page
    def view_books(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Available Books", font=("Arial", 16)).pack(pady=10)

        data = load_data()
        books = data["books"]

        tree = ttk.Treeview(self.main_frame, columns=("ID", "Title", "Author", "Category", "Copies"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Author")
        tree.heading("Category", text="Category")
        tree.heading("Copies", text="Copies")
        tree.pack(fill=tk.BOTH, expand=True)

        for book in books:
            tree.insert("", "end", values=(book["id"], book["title"], book["author"], book["category"], book["available_copies"]))

        tk.Button(self.main_frame, text="Back", command=self.show_dashboard).pack(pady=5)

    # Add Book Page (Admin)
    def add_book_page(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Add Book", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Book ID:").pack()
        self.book_id_entry = tk.Entry(self.main_frame)
        self.book_id_entry.pack()

        tk.Label(self.main_frame, text="Title:").pack()
        self.book_title_entry = tk.Entry(self.main_frame)
        self.book_title_entry.pack()

        tk.Label(self.main_frame, text="Author:").pack()
        self.book_author_entry = tk.Entry(self.main_frame)
        self.book_author_entry.pack()

        tk.Label(self.main_frame, text="Category:").pack()
        self.book_category_entry = tk.Entry(self.main_frame)
        self.book_category_entry.pack()

        tk.Label(self.main_frame, text="Available Copies:").pack()
        self.book_copies_entry = tk.Entry(self.main_frame)
        self.book_copies_entry.pack()

        tk.Button(self.main_frame, text="Add Book", command=self.add_book).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.show_dashboard).pack()

    # Add Book Function
    def add_book(self):
        book_id = self.book_id_entry.get()
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        category = self.book_category_entry.get()
        copies = self.book_copies_entry.get()

        if not (book_id and title and author and category and copies):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            copies = int(copies)
        except ValueError:
            messagebox.showerror("Error", "Copies must be a number!")
            return

        data = load_data()
        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "category": category,
            "available_copies": copies,
        }

        data["books"].append(new_book)
        save_data(data)
        messagebox.showinfo("Success", "Book added successfully!")
        self.show_dashboard()

    # Register User Function
    def register_user(self):
        user_type = self.register_type_entry.get()
        uid = self.register_uid_entry.get()
        name = self.register_name_entry.get()
        department = self.register_department_entry.get()
        email = self.register_email_entry.get()
        phone = self.register_phone_entry.get()
        password = self.register_password_entry.get()

        if not (user_type and uid and name and department and email and phone and password):
            messagebox.showerror("Error", "All fields are required!")
            return

        data = load_data()
        if any(user["email"] == email for user in data["users"]):
            messagebox.showerror("Error", "Email already registered!")
            return

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        new_user = {
            "uid": uid,
            "user_type": user_type,
            "name": name,
            "department": department,
            "email": email,
            "phone": phone,
            "password": hashed_password,
        }

        data["users"].append(new_user)
        save_data(data)
        messagebox.showinfo("Success", "Account registered successfully!")
        self.show_login_page()

    # Login User Function
    def login_user(self):
        email = self.login_email_entry.get()
        password = self.login_password_entry.get()

        if not (email and password):
            messagebox.showerror("Error", "All fields are required!")
            return

        data = load_data()
        for user in data["users"]:
            if user["email"] == email and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
                self.current_user = user
                self.show_dashboard()
                return

        messagebox.showerror("Error", "Invalid email or password!")

    # Logout Function
    def logout(self):
        self.current_user = None
        self.show_login_page()

    # Clear Frame
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


# Run the application
if __name__ == "__main__":
    initialize_db()
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
