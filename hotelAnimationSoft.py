import tkinter as tk
from tkinter import messagebox
import datetime


class Room:
    def __init__(self, room_number, room_type, ac, base_rate):
        self.room_number = room_number
        self.room_type = room_type  # 'single' or 'double'
        self.ac = ac  # True for AC, False for Non-AC
        self.base_rate = base_rate
        self.is_occupied = False


class Guest:
    def __init__(self, name, token_number, arrival_time, duration, room_type, ac, advance_paid):
        self.name = name
        self.token_number = token_number
        self.arrival_time = arrival_time
        self.duration = duration
        self.room_type = room_type
        self.ac = ac
        self.advance_paid = advance_paid
        self.room_number = None
        self.bill = 0


class HotelAutomation:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.token_counter = 1
        self.frequent_guest_discounts = {}

    def add_room(self, room_number, room_type, ac, base_rate):
        room = Room(room_number, room_type, ac, base_rate)
        self.rooms.append(room)

    def reserve_room(self, guest_name, arrival_time, duration, room_type, ac, advance_paid):
        for room in self.rooms:
            if not room.is_occupied and room.room_type == room_type and room.ac == ac:
                token_number = self.token_counter
                self.token_counter += 1
                guest = Guest(guest_name, token_number, arrival_time, duration, room_type, ac, advance_paid)
                guest.room_number = room.room_number
                room.is_occupied = True
                self.guests.append(guest)
                return f"Room {room.room_number} allocated to {guest_name}. Token: {token_number}"
        return "Apologies, no suitable room is available."

    def checkout(self, token_number):
        for guest in self.guests:
            if guest.token_number == token_number:
                room_number = guest.room_number
                room = next((room for room in self.rooms if room.room_number == room_number), None)
                if room:
                    room.is_occupied = False
                total_bill = guest.bill
                discount = self.frequent_guest_discounts.get(guest.name, 0)
                final_bill = total_bill * (1 - discount / 100)
                balance = max(0, final_bill - guest.advance_paid)
                self.guests.remove(guest)
                return f"Guest {guest.name} checked out. Total: {total_bill:.2f}, Discount: {discount}%, Final: {final_bill:.2f}, Balance: {balance:.2f}"
        return f"No guest found with token {token_number}."


class HotelGUI:
    def __init__(self, master, hotel):
        self.master = master
        self.hotel = hotel
        master.title("Hotel Automation System")
        master.configure(bg="lightblue")
        master.attributes('-fullscreen', True)

        # Main outer frame (bold black border)
        self.outer_frame = tk.Frame(master, bg="black", bd=10, relief="solid")
        self.outer_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=600)

        # Middle frame (bold white border)
        self.middle_frame = tk.Frame(self.outer_frame, bg="white", bd=10, relief="solid")
        self.middle_frame.pack(expand=True, fill="both", padx=5, pady=5)

        # Inner frame (content area)
        self.inner_frame = tk.Frame(self.middle_frame, bg="lightblue", bd=5)
        self.inner_frame.pack(expand=True, fill="both")

        # Reserve Room Section
        self.reserve_label = tk.Label(self.inner_frame, text="Reserve Room", bg="lightblue", font=("Helvetica", 16, "bold"))
        self.reserve_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(self.inner_frame, text="Name:", bg="lightblue", font=("Helvetica", 12))
        self.name_label.grid(row=1, column=0, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.inner_frame)
        self.name_entry.grid(row=1, column=1, pady=5, sticky="w")

        self.room_type_label = tk.Label(self.inner_frame, text="Room Type (single/double):", bg="lightblue", font=("Helvetica", 12))
        self.room_type_label.grid(row=2, column=0, pady=5, sticky="e")
        self.room_type_entry = tk.Entry(self.inner_frame)
        self.room_type_entry.grid(row=2, column=1, pady=5, sticky="w")

        self.ac_label = tk.Label(self.inner_frame, text="AC (yes/no):", bg="lightblue", font=("Helvetica", 12))
        self.ac_label.grid(row=3, column=0, pady=5, sticky="e")
        self.ac_entry = tk.Entry(self.inner_frame)
        self.ac_entry.grid(row=3, column=1, pady=5, sticky="w")

        self.advance_label = tk.Label(self.inner_frame, text="Advance Paid:", bg="lightblue", font=("Helvetica", 12))
        self.advance_label.grid(row=4, column=0, pady=5, sticky="e")
        self.advance_entry = tk.Entry(self.inner_frame)
        self.advance_entry.grid(row=4, column=1, pady=5, sticky="w")

        self.reserve_button = tk.Button(self.inner_frame, text="Reserve", command=self.reserve_room, bg="green", fg="white", font=("Helvetica", 12))
        self.reserve_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Checkout Section
        self.checkout_label = tk.Label(self.inner_frame, text="Checkout", bg="lightblue", font=("Helvetica", 16, "bold"))
        self.checkout_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.token_label = tk.Label(self.inner_frame, text="Token Number:", bg="lightblue", font=("Helvetica", 12))
        self.token_label.grid(row=7, column=0, pady=5, sticky="e")
        self.token_entry = tk.Entry(self.inner_frame)
        self.token_entry.grid(row=7, column=1, pady=5, sticky="w")

        self.checkout_button = tk.Button(self.inner_frame, text="Checkout", command=self.checkout_guest, bg="red", fg="white", font=("Helvetica", 12))
        self.checkout_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.close_button = tk.Button(self.inner_frame, text="Close", command=master.destroy, bg="black", fg="white", font=("Helvetica", 12))
        self.close_button.grid(row=9, column=0, columnspan=2, pady=10)

    def reserve_room(self):
        name = self.name_entry.get()
        room_type = self.room_type_entry.get()
        ac = self.ac_entry.get().lower() == "yes"
        advance_paid = float(self.advance_entry.get())

        result = self.hotel.reserve_room(name, datetime.datetime.now(), 3, room_type, ac, advance_paid)
        messagebox.showinfo("Reservation", result)

    def checkout_guest(self):
        token_number = int(self.token_entry.get())
        result = self.hotel.checkout(token_number)
        messagebox.showinfo("Checkout", result)


# Initialize hotel and GUI
hotel = HotelAutomation()
hotel.add_room(101, "single", True, 1000)
hotel.add_room(102, "double", False, 1500)
hotel.add_room(103, "single", False, 800)
hotel.add_room(104, "double", True, 2000)

root = tk.Tk()
hotel_gui = HotelGUI(root, hotel)
root.mainloop()
