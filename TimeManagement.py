import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Database setup
def initialize_db():
    conn = sqlite3.connect("tms.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            executive TEXT,
            invitees TEXT,
            venue TEXT,
            date TEXT,
            time TEXT,
            duration INTEGER,
            purpose TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Send email notification
def send_email(recipient, subject, body):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())

        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main Application Class
class TMSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Management Software")
        self.root.geometry("800x600")
        self.center_window()
        self.root.configure(bg="#e3f2fd")  # Light blue background

        # Header
        header = tk.Label(self.root, text="Time Management Software", font=("Arial", 24, "bold"), bg="#90caf9", fg="#0d47a1")
        header.pack(fill="x", pady=10)

        # Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Tab: Register Appointment
        self.register_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.register_tab, text="Register Appointment")
        self.create_register_tab()

        # Tab: View Statistics
        self.stats_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_tab, text="View Statistics")
        self.create_stats_tab()

        # Tab: Daily Schedule
        self.schedule_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.schedule_tab, text="Daily Schedule")
        self.create_schedule_tab()

        initialize_db()

    def center_window(self):
        """Centers the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_register_tab(self):
        frame = tk.Frame(self.register_tab, bg="#e3f2fd")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Input Fields
        fields = ["Executive Name", "Invitees", "Venue", "Date (YYYY-MM-DD)", "Time (HH:MM)", "Duration (mins)", "Purpose"]
        self.entries = {}

        for i, field in enumerate(fields):
            label = tk.Label(frame, text=field, font=("Arial", 14), bg="#e3f2fd", fg="#0d47a1")
            label.grid(row=i, column=0, sticky="e", pady=5, padx=10)

            entry = tk.Entry(frame, font=("Arial", 14), width=30, bd=2, relief="solid", bg="#ffffff", fg="#000000")
            entry.grid(row=i, column=1, pady=5)
            self.entries[field] = entry

        # Register Button
        register_button = tk.Button(frame, text="Register Appointment", font=("Arial", 14, "bold"), bg="#64b5f6", fg="white", command=self.register_appointment)
        register_button.grid(row=len(fields), columnspan=2, pady=20)

    def create_stats_tab(self):
        frame = tk.Frame(self.stats_tab, bg="#e3f2fd")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.stats_text = tk.Text(frame, font=("Arial", 12), height=20, width=70, state="disabled", wrap="word", bg="#ffffff", fg="#000000")
        self.stats_text.pack(pady=10)

        stats_button = tk.Button(frame, text="Generate Statistics", font=("Arial", 14, "bold"), bg="#64b5f6", fg="white", command=self.generate_statistics)
        stats_button.pack(pady=10)

    def create_schedule_tab(self):
        frame = tk.Frame(self.schedule_tab, bg="#e3f2fd")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.schedule_text = tk.Text(frame, font=("Arial", 12), height=20, width=70, state="disabled", wrap="word", bg="#ffffff", fg="#000000")
        self.schedule_text.pack(pady=10)

        schedule_button = tk.Button(frame, text="Show Today's Schedule", font=("Arial", 14, "bold"), bg="#64b5f6", fg="white", command=self.show_schedule)
        schedule_button.pack(pady=10)

    def register_appointment(self):
        # Collect data from entries
        data = {field: entry.get().strip() for field, entry in self.entries.items()}

        # Validate inputs
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("tms.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO appointments (executive, invitees, venue, date, time, duration, purpose) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (data["Executive Name"], data["Invitees"], data["Venue"], data["Date (YYYY-MM-DD)"], data["Time (HH:MM)"], data["Duration (mins)"], data["Purpose"]))
            conn.commit()
            conn.close()

            # Send email notification
            self.send_appointment_email(data)

            messagebox.showinfo("Success", "Appointment registered successfully!")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to register appointment: {e}")

    def send_appointment_email(self, data):
        subject = "New Appointment Registered"
        body = (f"Executive: {data['Executive Name']}\n"
                f"Invitees: {data['Invitees']}\n"
                f"Venue: {data['Venue']}\n"
                f"Date: {data['Date (YYYY-MM-DD)']}\n"
                f"Time: {data['Time (HH:MM)']}\n"
                f"Duration: {data['Duration (mins)']} minutes\n"
                f"Purpose: {data['Purpose']}")

        send_email("recipient@example.com", subject, body)

    def generate_statistics(self):
        try:
            conn = sqlite3.connect("tms.db")
            cursor = conn.cursor()
            cursor.execute("SELECT executive, COUNT(*), SUM(duration) FROM appointments GROUP BY executive")
            stats = cursor.fetchall()
            conn.close()

            self.stats_text.config(state="normal")
            self.stats_text.delete(1.0, tk.END)

            for stat in stats:
                self.stats_text.insert(tk.END, f"Executive: {stat[0]}\nMeetings: {stat[1]}\nTotal Time: {stat[2]} minutes\n\n")

            self.stats_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate statistics: {e}")

    def show_schedule(self):
        try:
            today = datetime.date.today().strftime("%Y-%m-%d")
            conn = sqlite3.connect("tms.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM appointments WHERE date = ?", (today,))
            schedule = cursor.fetchall()
            conn.close()

            self.schedule_text.config(state="normal")
            self.schedule_text.delete(1.0, tk.END)

            for entry in schedule:
                self.schedule_text.insert(tk.END, f"Executive: {entry[1]}\nInvitees: {entry[2]}\nVenue: {entry[3]}\nTime: {entry[5]}\nDuration: {entry[6]} minutes\nPurpose: {entry[7]}\n\n")

            self.schedule_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show schedule: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TMSApp(root)
    root.mainloop()
