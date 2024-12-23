import datetime

# Data storage for trucks, consignments, and offices
trucks = []  # List of trucks
consignments = []  # List of consignments
offices = ["Head Office", "Branch A", "Branch B", "Branch C"]  # Branch offices

# Constants
VOLUME_THRESHOLD = 500  # Volume threshold for truck allocation
TRUCK_CAPACITY = 500  # Capacity of a truck in cubic meters
TRANSPORT_RATE = 10  # Charge per cubic meter


# Initialize trucks
def initialize_trucks():
    global trucks
    for i in range(1, 6):  # Adding 5 trucks for simplicity
        trucks.append({
            "id": f"TRUCK-{i}",
            "current_location": "Head Office",
            "status": "Available",  # Available, In Transit, or Idle
            "loaded_volume": 0,
            "destination": None,
            "dispatch_date": None,
            "arrival_date": None,
            "idle_days": 0
        })


# Function to accept a new consignment
def accept_consignment():
    print("\n--- Accept New Consignment ---")
    sender = input("Enter sender's name: ")
    sender_address = input("Enter sender's address: ")
    receiver = input("Enter receiver's name: ")
    receiver_address = input("Enter receiver's address: ")
    destination = input(f"Enter destination office ({', '.join(offices)}): ")
    volume = float(input("Enter consignment volume (cubic meters): "))
    
    if destination not in offices:
        print("Invalid destination!")
        return

    consignment = {
        "id": len(consignments) + 1,
        "sender": sender,
        "sender_address": sender_address,
        "receiver": receiver,
        "receiver_address": receiver_address,
        "destination": destination,
        "volume": volume,
        "charge": volume * TRANSPORT_RATE,
        "status": "Pending",  # Pending or Dispatched
        "accepted_date": datetime.date.today(),
        "dispatch_date": None
    }
    consignments.append(consignment)
    print(f"Consignment accepted successfully! Bill Amount: Rs. {consignment['charge']}")


# Function to check and allocate trucks
def allocate_trucks():
    print("\n--- Truck Allocation ---")
    destination_volumes = {office: 0 for office in offices}
    pending_consignment = []

    # Calculate total pending volume for each destination
    for consignment in consignments:
        if consignment["status"] == "Pending":
            destination_volumes[consignment["destination"]] += consignment["volume"]
            pending_consignment.append(consignment)

    # Allocate trucks for destinations exceeding the volume threshold
    for destination, volume in destination_volumes.items():
        if volume >= VOLUME_THRESHOLD:
            truck = next((t for t in trucks if t["status"] == "Available"), None)
            if truck:
                print(f"Allocating {truck['id']} to {destination} with volume: {volume} cubic meters")
                truck["status"] = "In Transit"
                truck["loaded_volume"] = volume
                truck["destination"] = destination
                truck["dispatch_date"] = datetime.date.today()

                # Mark consignments as dispatched
                for consignment in pending_consignment:
                    if consignment["destination"] == destination:
                        consignment["status"] = "Dispatched"
                        consignment["dispatch_date"] = datetime.date.today()
            else:
                print("No trucks available for allocation at the moment.")


# Function to view truck status
def view_truck_status():
    print("\n--- Truck Status ---")
    print(f"{'Truck ID':<10} {'Location':<15} {'Status':<10} {'Loaded Volume':<15} {'Destination':<12}")
    for truck in trucks:
        print(f"{truck['id']:<10} {truck['current_location']:<15} {truck['status']:<10} {truck['loaded_volume']:<15} {truck['destination'] or 'N/A':<12}")


# Function to query consignments
def query_consignments():
    print("\n--- Query Consignments ---")
    print(f"{'ID':<5} {'Volume':<10} {'Sender':<12} {'Receiver':<12} {'Destination':<12} {'Status':<10}")
    for consignment in consignments:
        print(f"{consignment['id']:<5} {consignment['volume']:<10} {consignment['sender']:<12} "
              f"{consignment['receiver']:<12} {consignment['destination']:<12} {consignment['status']:<10}")


# Function to calculate statistics
def generate_statistics():
    print("\n--- Statistics Report ---")
    total_revenue = sum(c["charge"] for c in consignments)
    avg_waiting_days = 0
    dispatched_count = len([c for c in consignments if c["status"] == "Dispatched"])
    pending_count = len([c for c in consignments if c["status"] == "Pending"])

    print(f"Total Revenue: Rs. {total_revenue}")
    print(f"Total Consignments Dispatched: {dispatched_count}")
    print(f"Pending Consignments: {pending_count}")


# Main menu
def main():
    initialize_trucks()
    while True:
        print("\n--- Transport Company Computerization System ---")
        print("1. Accept New Consignment")
        print("2. Allocate Trucks for Dispatch")
        print("3. View Truck Status")
        print("4. Query Consignments")
        print("5. Generate Statistics Report")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            accept_consignment()
        elif choice == '2':
            allocate_trucks()
        elif choice == '3':
            view_truck_status()
        elif choice == '4':
            query_consignments()
        elif choice == '5':
            generate_statistics()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
