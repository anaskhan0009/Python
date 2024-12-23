import datetime

class Room:
    def __init__(self, room_number, room_type, ac_type, rate):
        self.room_number = room_number
        self.room_type = room_type  # 'single' or 'double'
        self.ac_type = ac_type      # 'AC' or 'Non-AC'
        self.rate = rate            # Tariff rate for the room
        self.occupied = False       # Availability status

class Hotel:
    def __init__(self, total_rooms):
        self.rooms = self.generate_rooms(total_rooms)
        self.guests = {}
        self.food_items = {'breakfast': 50, 'lunch': 100, 'dinner': 150}  # Sample food prices
        self.discount_rate = 0.10   # 10% discount for frequent guests

    def generate_rooms(self, total_rooms):
        rooms = []
        for room_number in range(1, total_rooms + 1):
            room_type = 'single' if room_number % 2 == 0 else 'double'  # For simplicity, alternate room types
            ac_type = 'AC' if room_number % 3 == 0 else 'Non-AC'      # Every 3rd room is AC
            rate = 2000 if room_type == 'single' else 3000
            rooms.append(Room(room_number, room_type, ac_type, rate))
        return rooms

    def check_availability(self, room_type, ac_type):
        for room in self.rooms:
            if not room.occupied and room.room_type == room_type and room.ac_type == ac_type:
                return room
        return None

    def reserve_room(self, guest_name, room_type, ac_type, duration, advance_paid):
        room = self.check_availability(room_type, ac_type)
        if room:
            room.occupied = True
            guest_token = len(self.guests) + 1  # Simple token generation
            guest = {'name': guest_name, 'room_number': room.room_number, 'duration': duration,
                     'advance_paid': advance_paid, 'room_rate': room.rate, 'total_bill': 0}
            self.guests[guest_token] = guest
            return guest_token, room.room_number
        else:
            return None, None

    def calculate_total_bill(self, guest_token):
        guest = self.guests[guest_token]
        stay_cost = guest['room_rate'] * guest['duration']
        food_cost = guest['total_bill']
        total_cost = stay_cost + food_cost
        # Apply discount for frequent guests (example: guest_token <= 10 is considered frequent)
        if guest_token <= 10:
            total_cost -= total_cost * self.discount_rate
        return total_cost

    def add_food_consumption(self, guest_token, food_type, quantity):
        if guest_token in self.guests and food_type in self.food_items:
            food_price = self.food_items[food_type] * quantity
            self.guests[guest_token]['total_bill'] += food_price
            return f"Added {quantity} {food_type}(s) for guest {guest_token}."
        else:
            return "Invalid food type or guest token."

    def checkout(self, guest_token):
        if guest_token in self.guests:
            guest = self.guests.pop(guest_token)
            total_bill = self.calculate_total_bill(guest_token)
            balance_due = total_bill - guest['advance_paid']
            room_number = guest['room_number']
            self.rooms[room_number - 1].occupied = False  # Mark room as available again
            return total_bill, balance_due
        else:
            return "Guest not found!"

    def print_room_details(self):
        for room in self.rooms:
            status = 'Occupied' if room.occupied else 'Available'
            print(f"Room {room.room_number} - {room.room_type} - {room.ac_type} - Rate: {room.rate} - Status: {status}")

# Main System
def main():
    hotel = Hotel(10)  # Create a hotel with 10 rooms

    while True:
        print("\n--- (Hotel Automation Software) ---")
        print("1. View Available Rooms")
        print("2. Reserve Room")
        print("3. Add Food Consumption")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            hotel.print_room_details()

        elif choice == "2":
            guest_name = input("Enter guest name: ").strip()
            room_type = input("Enter room type ('single' or 'double'): ").strip()
            ac_type = input("Enter AC type ('AC' or 'Non-AC'): ").strip()
            duration = int(input("Enter duration of stay (in days): ").strip())
            advance_paid = float(input("Enter advance paid: ").strip())
            token, room_number = hotel.reserve_room(guest_name, room_type, ac_type, duration, advance_paid)
            if token:
                print(f"Room reserved successfully! Token number: {token}, Room number: {room_number}")
            else:
                print("Sorry, no room available for your preference.")

        elif choice == "3":
            guest_token = int(input("Enter guest token number: ").strip())
            food_type = input("Enter food type ('breakfast', 'lunch', 'dinner'): ").strip()
            quantity = int(input("Enter quantity: ").strip())
            print(hotel.add_food_consumption(guest_token, food_type, quantity))

        elif choice == "4":
            guest_token = int(input("Enter guest token number: ").strip())
            total_bill, balance_due = hotel.checkout(guest_token)
            if isinstance(total_bill, str):
                print(total_bill)
            else:
                print(f"Total Bill: {total_bill}, Balance Due: {balance_due}")

        elif choice == "5":
            print("Exiting the Hotel Automation System. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
