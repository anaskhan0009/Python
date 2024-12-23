import tkinter as tk
from tkinter import messagebox

# Book and Student Classes
class Book:
    def __init__(self, bno=" ", bname=" ", auname=" "):
        self.bno = bno
        self.bname = bname
        self.auname = auname
        self.is_issued = False  # Track if the book is issued or not
    
    def create_book(self, bno, bname, auname):
        self.bno = bno
        self.bname = bname
        self.auname = auname
    
    def show_book(self):
        return f"Book Number: {self.bno}, Name: {self.bname}, Author: {self.auname}"

class Student:
    def __init__(self, admno=" ", name=" ", stbno=" ", token=0):
        self.admno = admno
        self.name = name
        self.stbno = stbno
        self.token = token
    
    def create_student(self, admno, name):
        self.admno = admno
        self.name = name
        self.token = 0
    
    def show_student(self):
        return f"Admission No: {self.admno}, Name: {self.name}, Token: {self.token}"

# Prepopulating books and students
students = [Student(str(i), f"Student {i}") for i in range(1, 21)]  # 20 sample students
books = [Book(str(i), f"Programming Book {i}", "Author") for i in range(1, 1001)]  # 1000 books

# GUI Functionality
class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("A & A Library Management")
        
        # Set the background color to green
        self.root.config(bg="green")  # Root window background color
        self.frame = tk.Frame(self.root, bg="green")  # Frame background color
        self.frame.pack(padx=10, pady=10)

        # Add buttons for actions
        self.create_widgets()

    def create_widgets(self):
        # Main menu button
        self.main_menu_button = tk.Button(self.frame, text="Main Menu", command=self.main_menu)
        self.main_menu_button.grid(row=0, column=0, padx=5, pady=5)

        # Admin menu button
        self.admin_button = tk.Button(self.frame, text="Admin Menu", command=self.admin_menu)
        self.admin_button.grid(row=1, column=0, padx=5, pady=5)

        # Student menu button
        self.student_button = tk.Button(self.frame, text="Student Menu", command=self.student_menu)
        self.student_button.grid(row=1, column=1, padx=5, pady=5)

    def main_menu(self):
        self.clear_frame()
        self.main_label = tk.Label(self.frame, text="Library Main Menu", font=("Arial", 16), bg="green")
        self.main_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.admin_button = tk.Button(self.frame, text="Admin Menu", command=self.admin_menu)
        self.admin_button.grid(row=1, column=0, padx=5, pady=5)

        self.student_button = tk.Button(self.frame, text="Student Menu", command=self.student_menu)
        self.student_button.grid(row=1, column=1, padx=5, pady=5)

    def admin_menu(self):
        self.clear_frame()
        self.admin_label = tk.Label(self.frame, text="Admin Menu", font=("Arial", 16), bg="green")
        self.admin_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_book_button = tk.Button(self.frame, text="Create Book", command=self.create_book)
        self.create_book_button.grid(row=1, column=0, padx=5, pady=5)

        self.create_student_button = tk.Button(self.frame, text="Create Student", command=self.create_student)
        self.create_student_button.grid(row=1, column=1, padx=5, pady=5)

        # Manage Books button
        self.manage_books_button = tk.Button(self.frame, text="Manage Books", command=self.manage_books)
        self.manage_books_button.grid(row=2, column=0, padx=5, pady=5)

        # Adding a button to go back to the main menu
        self.back_to_main_button = tk.Button(self.frame, text="Back to Main Menu", command=self.main_menu)
        self.back_to_main_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def student_menu(self):
        self.clear_frame()
        self.student_label = tk.Label(self.frame, text="Student Menu", font=("Arial", 16), bg="green")
        self.student_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.display_students_button = tk.Button(self.frame, text="Display Students", command=self.display_students)
        self.display_students_button.grid(row=1, column=0, padx=5, pady=5)

        self.display_books_button = tk.Button(self.frame, text="Display Books", command=self.display_books)
        self.display_books_button.grid(row=1, column=1, padx=5, pady=5)

        self.issue_book_button = tk.Button(self.frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.grid(row=2, column=0, padx=5, pady=5)

        self.return_book_button = tk.Button(self.frame, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=2, column=1, padx=5, pady=5)

        # Adding the "Back to Main Menu" button in the Student Menu
        self.back_to_main_button = tk.Button(self.frame, text="Back to Main Menu", command=self.main_menu)
        self.back_to_main_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def manage_books(self):
        self.clear_frame()
        self.manage_books_label = tk.Label(self.frame, text="Manage Books", font=("Arial", 16), bg="green")
        self.manage_books_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.remove_book_button = tk.Button(self.frame, text="Remove Book", command=self.remove_book)
        self.remove_book_button.grid(row=1, column=0, padx=5, pady=5)

        self.display_books_button = tk.Button(self.frame, text="Display Books", command=self.display_books)
        self.display_books_button.grid(row=1, column=1, padx=5, pady=5)

        self.back_to_admin_button = tk.Button(self.frame, text="Back to Admin Menu", command=self.admin_menu)
        self.back_to_admin_button.grid(row=2, column=0, columnspan=2, pady=10)

    def remove_book(self):
        self.clear_frame()
        self.remove_label = tk.Label(self.frame, text="Remove Book", font=("Arial", 16), bg="green")
        self.remove_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create Listbox to display books
        self.book_listbox = tk.Listbox(self.frame, height=15, width=60)
        for book in books:
            self.book_listbox.insert(tk.END, f"{book.bno} - {book.bname} by {book.auname}")
        self.book_listbox.grid(row=1, column=0, columnspan=2, pady=5)

        self.remove_button = tk.Button(self.frame, text="Remove Selected Book", command=self.remove_selected_book)
        self.remove_button.grid(row=2, column=0, padx=5, pady=5)

        self.back_button = tk.Button(self.frame, text="Back to Manage Books", command=self.manage_books)
        self.back_button.grid(row=2, column=1, padx=5, pady=5)

    def remove_selected_book(self):
        try:
            selected_book_index = self.book_listbox.curselection()[0]
            selected_book = books[selected_book_index]
            
            # Confirm removal
            confirm = messagebox.askyesno("Confirm Removal", f"Are you sure you want to remove '{selected_book.bname}'?")
            if confirm:
                books.remove(selected_book)
                messagebox.showinfo("Success", f"Book '{selected_book.bname}' removed successfully.")
                self.remove_book()  # Refresh the remove book menu to update the list
        except IndexError:
            messagebox.showwarning("Warning", "Please select a book to remove.")

    def display_books(self):
        self.clear_frame()
        self.book_label = tk.Label(self.frame, text="Book List", font=("Arial", 16), bg="green")
        self.book_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create Listbox to display books
        self.book_listbox = tk.Listbox(self.frame, height=10, width=50)
        for book in books[:10]:  # Displaying first 10 books
            self.book_listbox.insert(tk.END, f"{book.bno} - {book.bname} by {book.auname}")
        self.book_listbox.grid(row=1, column=0, columnspan=2, pady=5)

        self.exit_button = tk.Button(self.frame, text="Back to Admin Menu", command=self.admin_menu)
        self.exit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def display_students(self):
        self.clear_frame()
        self.student_label = tk.Label(self.frame, text="Student List", font=("Arial", 16), bg="green")
        self.student_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create Listbox to display students
        self.student_listbox = tk.Listbox(self.frame, height=10, width=50)
        for student in students[:10]:  # Displaying first 10 students
            self.student_listbox.insert(tk.END, f"{student.admno} - {student.name}")
        self.student_listbox.grid(row=1, column=0, columnspan=2, pady=5)

        self.exit_button = tk.Button(self.frame, text="Back to Admin Menu", command=self.admin_menu)
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
        books.append(Book(book_number, book_name, author_name))
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
        
        # Add student to the list
        students.append(Student(student_admno, student_name))
        messagebox.showinfo("Success", f"Student '{student_name}' added successfully.")
        window.destroy()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# Initialize the Tkinter application
root = tk.Tk()
app = LibraryGUI(root)
root.mainloop()
