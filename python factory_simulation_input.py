import random

# Define the Machine class
class Machine:
    def __init__(self, machine_id, category, mttf):
        self.id = machine_id
        self.category = category
        self.mttf = mttf  # Mean Time To Failure
        self.down_time = 0  # Time the machine waits for repair
        self.fail_time = random.randint(1, mttf)  # Random failure time

# Define the Adjuster class
class Adjuster:
    def __init__(self, adjuster_id):
        self.id = adjuster_id
        self.busy_until = 0  # Time until the adjuster is busy

# Main Factory Simulation
def factory_simulation(machines, adjusters, simulation_time):
    current_time = 0
    repairs_done = 0

    print("\n--- Factory Machine Simulation Started ---\n")
    
    while current_time <= simulation_time:
        # Check for machine failures
        for machine in machines:
            if machine.fail_time <= current_time:
                print(f"Time {current_time}: Machine {machine.id} ({machine.category}) failed.")

                # Check for an available adjuster
                for adjuster in adjusters:
                    if adjuster.busy_until <= current_time:
                        repair_time = random.randint(1, 3)  # Repair time: 1-3 hours
                        adjuster.busy_until = current_time + repair_time
                        machine.fail_time = current_time + random.randint(1, machine.mttf)  # Next failure time
                        machine.down_time += repair_time
                        repairs_done += 1
                        print(f"  Adjuster {adjuster.id} is repairing Machine {machine.id} (Repair Time: {repair_time} hrs)")
                        break
                else:
                    print(f"  No adjuster is available! Machine {machine.id} is waiting for repair.")

        current_time += 1  # Increment time

    # Summary
    print("\n--- Simulation Summary ---")
    for machine in machines:
        print(f"Machine {machine.id} ({machine.category}) - Total Down Time: {machine.down_time} hrs")
    print(f"Total Repairs Completed: {repairs_done}")
    print("\n--- End of Simulation ---")

# Input Section
def get_user_input():
    machines = []
    adjusters = []

    print("Factory Machine Simulation Setup:\n")
    
    # Get machine details
    num_machines = int(input("Enter the number of machines: "))
    for i in range(1, num_machines + 1):
        category = input(f"Enter the category of Machine {i}: ")
        mttf = int(input(f"Enter the Mean Time To Failure (MTTF) for Machine {i} (in hours): "))
        machines.append(Machine(i, category, mttf))

    # Get adjuster details
    num_adjusters = int(input("\nEnter the number of adjusters: "))
    for i in range(1, num_adjusters + 1):
        adjusters.append(Adjuster(i))

    # Get simulation time
    simulation_time = int(input("\nEnter the total simulation time (in hours): "))

    return machines, adjusters, simulation_time

# Run the program
if __name__ == "__main__":
    machines, adjusters, simulation_time = get_user_input()
    factory_simulation(machines, adjusters, simulation_time)
