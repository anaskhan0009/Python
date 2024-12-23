import tkinter as tk
from tkinter import messagebox
from pickle import load, dump
from os import remove, rename
import os

# Create a basic class for book and student (as you have in the original code)
class Book:
    def __init__(self, bno=" ", bname=" ", auname=" "):
        self.bno = bno
        self.bname = bname
        self.auname = auname
    
    def create_book(self):
        self.bno = input("\t Enter Book Number:")
        self.bname = input("\t Enter Name of the Book:")
        self.auname = input("\t Enter Name of the Author:")
        print("\t Book Created")

    def show_book(self):
        return f"Book Number: {self.bno}, Name: {self.bname}, Author: {self.auname}"
    
    def modify_book(self):
        self.bname = input("\t Enter New Book Name:")
        self.auname = input("\t Enter New Author Name:")

class Student:
    def __init__(self, admno=" ", name=" ", stbno=" ", token=0):
        self.admno = admno
        self.name = name
        self.stbno = stbno
        self.token = token
    
    def create_student(self):
        self.admno = input("\t Enter Admission Number:")
        self.name = input("\t Enter Name of the Student:")
        self.token = 0
    
    def show_student(self):
        return f"Admission No: {self.admno}, Name: {self.name}, Token: {self.token}"

# GUI Functionality
class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("A & A Library Management")
        
        # Main Frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Add buttons for actions
        self.create_widgets()

    def create_widgets(self):
        # Admin menu button
        self.admin_button = tk.Button(self.frame, text="Admin Menu", command=self.admin_menu)
        self.admin_button.grid(row=0, column=0, padx=5, pady=5)

        # Student menu button
        self.student_button = tk.Button(self.frame, text="Student Menu", command=self.student_menu)
        self.student_button.grid(row=0, column=1, padx=5, pady=5)

    def admin_menu(self):
        self.clear_frame()
        self.admin_label = tk.Label(self.frame, text="Admin Menu", font=("Arial", 16))
        self.admin_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_book_button = tk.Button(self.frame, text="Create Book", command=self.create_book)
        self.create_book_button.grid(row=1, column=0, padx=5, pady=5)

        self.create_student_button = tk.Button(self.frame, text="Create Student", command=self.create_student)
        self.create_student_button.grid(row=1, column=1, padx=5, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def student_menu(self):
        self.clear_frame()
        self.student_label = tk.Label(self.frame, text="Student Menu", font=("Arial", 16))
        self.student_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.issue_book_button = tk.Button(self.frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.grid(row=1, column=0, padx=5, pady=5)

        self.return_book_button = tk.Button(self.frame, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=1, column=1, padx=5, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def create_book(self):
        # For now, we'll just display a message as we are focusing on the GUI part
        book_window = tk.Toplevel(self.root)
        book_window.title("Create Book")
        
        self.book_bno_label = tk.Label(book_window, text="Enter Book Number:")
        self.book_bno_label.grid(row=0, column=0)
        self.book_bno_entry = tk.Entry(book_window)
        self.book_bno_entry.grid(row=0, column=1)

        self.book_name_label = tk.Label(book_window, text="Enter Book Name:")
        self.book_name_label.grid(row=1, column=0)
        self.book_name_entry = tk.Entry(book_window)
        self.book_name_entry.grid(row=1, column=1)

        self.book_author_label = tk.Label(book_window, text="Enter Author Name:")
        self.book_author_label.grid(row=2, column=0)
        self.book_author_entry = tk.Entry(book_window)
        self.book_author_entry.grid(row=2, column=1)

        self.save_button = tk.Button(book_window, text="Save Book", command=lambda: self.save_book(book_window))
        self.save_button.grid(row=3, column=0, columnspan=2)

    def save_book(self, window):
        # Get book details and close window
        book_number = self.book_bno_entry.get()
        book_name = self.book_name_entry.get()
        author_name = self.book_author_entry.get()
        
        # Here, you would save this data to your file or database
        messagebox.showinfo("Success", f"Book '{book_name}' added successfully.")
        window.destroy()

    def create_student(self):
        # Similar to create_book, implement GUI for student creation
        student_window = tk.Toplevel(self.root)
        student_window.title("Create Student")
        
        self.student_admno_label = tk.Label(student_window, text="Enter Admission Number:")
        self.student_admno_label.grid(row=0, column=0)
        self.student_admno_entry = tk.Entry(student_window)
        self.student_admno_entry.grid(row=0, column=1)

        self.student_name_label = tk.Label(student_window, text="Enter Student Name:")
        self.student_name_label.grid(row=1, column=0)
        self.student_name_entry = tk.Entry(student_window)
        self.student_name_entry.grid(row=1, column=1)

        self.save_button = tk.Button(student_window, text="Save Student", command=lambda: self.save_student(student_window))
        self.save_button.grid(row=2, column=0, columnspan=2)

    def save_student(self, window):
        student_admno = self.student_admno_entry.get()
        student_name = self.student_name_entry.get()
        
        # Here, you would save this data to your file or database
        messagebox.showinfo("Success", f"Student '{student_name}' added successfully.")
        window.destroy()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# Initialize the Tkinter application
root = tk.Tk()
app = LibraryGUI(root)
root.mainloop()
