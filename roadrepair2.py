import datetime

class RRTS:
    def __init__(self):
        self.complaints = []        # List to store complaints
        self.scheduled_repairs = [] # List to store scheduled repairs
        self.manpower = 0           # Manpower availability
        self.machines = 0           # Machines availability

    def add_complaint(self):
        complaint = input("Enter complaint details: ").strip()
        if complaint:
            self.complaints.append(complaint)
            print(f"Complaint added successfully: '{complaint}'")
        else:
            print("Error: Complaint cannot be empty.")

    def schedule_repair(self):
        if not self.complaints:
            print("No complaints available to schedule.")
            return
        
        print("\nComplaints List:")
        for i, complaint in enumerate(self.complaints, start=1):
            print(f"{i}. {complaint}")
        
        try:
            choice = int(input("Enter the number of the complaint to schedule for repair: "))
            if 1 <= choice <= len(self.complaints):
                scheduled_complaint = self.complaints.pop(choice - 1)
                self.scheduled_repairs.append(scheduled_complaint)
                print(f"Repair scheduled for: '{scheduled_complaint}'")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

    def update_resources(self):
        try:
            self.manpower = int(input("Enter available manpower: ").strip())
            self.machines = int(input("Enter available machines: ").strip())
            print(f"Resources updated: Manpower = {self.manpower}, Machines = {self.machines}")
        except ValueError:
            print("Error: Please enter valid numbers for resources.")

    def show_statistics(self):
        total_repairs = len(self.scheduled_repairs)
        pending_repairs = len(self.complaints)
        utilization = (total_repairs / (total_repairs + pending_repairs)) * 100 if (total_repairs + pending_repairs) > 0 else 0

        print("\n--- Repair Statistics ---")
        print(f"Repairs completed: {total_repairs}")
        print(f"Repairs pending: {pending_repairs}")
        print(f"Resource Utilization: {utilization:.2f}%")

def main():
    rrts = RRTS()
    
    while True:
        print("\n--- Road Repair and Tracking System (RRTS) ---")
        print("1. Register Complaint")
        print("2. Schedule Repair")
        print("3. Update Resources")
        print("4. Show Statistics")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            rrts.add_complaint()
        elif choice == "2":
            rrts.schedule_repair()
        elif choice == "3":
            rrts.update_resources()
        elif choice == "4":
            rrts.show_statistics()
        elif choice == "5":
            print("Exiting RRTS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
