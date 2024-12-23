class DepartmentInfoSystem:
    def __init__(self):
        self.students = {}
        self.inventory = {}
        self.accounts = {'income': 0, 'expenditure': 0}
        self.research_projects = {}
        self.publications = {}

    def add_student(self, roll_number, name, address, course_registered):
        """Add a student to the system."""
        self.students[roll_number] = {
            'name': name,
            'address': address,
            'course_registered': course_registered,
            'completed_courses': [],
            'backlog_courses': [],
            'grades': [],
            'gpa': 0.0,
            'cgpa': 0.0
        }
        print(f"Student {name} added successfully!")

    def register_courses(self, roll_number, courses):
        """Register courses for a student."""
        if roll_number in self.students:
            self.students[roll_number]['course_registered'].extend(courses)
            print(f"Courses registered for student {roll_number}.")
        else:
            print(f"Student with roll number {roll_number} not found.")

    def enter_grades(self, roll_number, grades):
        """Enter grades for a student."""
        if roll_number in self.students:
            self.students[roll_number]['grades'] = grades
            self.calculate_gpa(roll_number)
            print(f"Grades entered for student {roll_number}.")
        else:
            print(f"Student with roll number {roll_number} not found.")

    def calculate_gpa(self, roll_number):
        """Calculate GPA and CGPA for the student."""
        student = self.students[roll_number]
        total_grade_points = 0
        total_courses = len(student['grades'])

        for grade in student['grades']:
            total_grade_points += self.grade_to_points(grade)

        student['gpa'] = total_grade_points / total_courses if total_courses > 0 else 0.0
        student['cgpa'] = student['gpa']  # Assume CGPA is same as GPA for now
        print(f"GPA and CGPA calculated for student {roll_number}.")

    def grade_to_points(self, grade):
        """Convert letter grade to grade points."""
        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        return grade_points.get(grade.upper(), 0.0)

    def generate_grade_sheet(self, roll_number):
        """Generate grade sheet for a student."""
        if roll_number in self.students:
            student = self.students[roll_number]
            print(f"\nGrade Sheet for {student['name']}:")
            print(f"Roll Number: {roll_number}")
            print(f"Address: {student['address']}")
            print(f"Courses Registered: {', '.join(student['course_registered'])}")
            print(f"Completed Courses: {', '.join(student['completed_courses'])}")
            print(f"Backlog Courses: {', '.join(student['backlog_courses'])}")
            print(f"Grades: {', '.join(student['grades'])}")
            print(f"GPA: {student['gpa']}")
            print(f"CGPA: {student['cgpa']}")
        else:
            print(f"Student with roll number {roll_number} not found.")

    def add_inventory_item(self, item_id, name, location):
        """Add an item to the department inventory."""
        self.inventory[item_id] = {'name': name, 'location': location}
        print(f"Item {name} added to the inventory.")

    def update_inventory_item(self, item_id, new_location):
        """Update the location of an item in the inventory."""
        if item_id in self.inventory:
            self.inventory[item_id]['location'] = new_location
            print(f"Location of item {self.inventory[item_id]['name']} updated.")
        else:
            print(f"Item with ID {item_id} not found.")

    def display_inventory(self):
        """Display all items in the inventory."""
        print("\nDepartment Inventory:")
        for item_id, item in self.inventory.items():
            print(f"Item ID: {item_id}, Name: {item['name']}, Location: {item['location']}")

    def record_income(self, amount):
        """Record income from consultancy or grants."""
        self.accounts['income'] += amount
        print(f"Income of {amount} recorded.")

    def record_expenditure(self, amount):
        """Record expenditure of the department."""
        self.accounts['expenditure'] += amount
        print(f"Expenditure of {amount} recorded.")

    def generate_account_summary(self):
        """Generate financial summary (income, expenditure, balance)."""
        balance = self.accounts['income'] - self.accounts['expenditure']
        print(f"\nFinancial Summary:")
        print(f"Income: {self.accounts['income']}")
        print(f"Expenditure: {self.accounts['expenditure']}")
        print(f"Balance: {balance}")

    def add_research_project(self, project_id, title, description):
        """Add a research project to the department's record."""
        self.research_projects[project_id] = {'title': title, 'description': description}
        print(f"Research project {title} added.")

    def add_publication(self, faculty_name, publication_title, year):
        """Add a faculty publication to the records."""
        if faculty_name not in self.publications:
            self.publications[faculty_name] = []
        self.publications[faculty_name].append({'title': publication_title, 'year': year})
        print(f"Publication '{publication_title}' by {faculty_name} added.")

    def query_student(self, roll_number):
        """Query student details by roll number."""
        if roll_number in self.students:
            student = self.students[roll_number]
            print(f"\nStudent Details for {student['name']}:")
            print(f"Roll Number: {roll_number}")
            print(f"Courses Registered: {', '.join(student['course_registered'])}")
            print(f"GPA: {student['gpa']}")
            print(f"CGPA: {student['cgpa']}")
        else:
            print(f"Student with roll number {roll_number} not found.")

    def query_financials(self):
        """Query financial details."""
        self.generate_account_summary()


def print_menu():
    """Display the menu for the department system."""
    print("\n--- University Department Information System ---")
    print("1. Add Student")
    print("2. Register Courses")
    print("3. Enter Grades")
    print("4. Generate Grade Sheet")
    print("5. Add Inventory Item")
    print("6. Update Inventory Location")
    print("7. Display Inventory")
    print("8. Record Income")
    print("9. Record Expenditure")
    print("10. Generate Financial Summary")
    print("11. Add Research Project")
    print("12. Add Faculty Publication")
    print("13. Query Student Details")
    print("14. Query Financial Details")
    print("0. Exit")


def main():
    """Main function to run the university department system."""
    system = DepartmentInfoSystem()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            roll_number = int(input("Enter student roll number: "))
            name = input("Enter student name: ")
            address = input("Enter student address: ")
            course_registered = input("Enter courses registered (comma separated): ").split(",")
            system.add_student(roll_number, name, address, course_registered)

        elif choice == '2':
            roll_number = int(input("Enter student roll number: "))
            courses = input("Enter courses to register (comma separated): ").split(",")
            system.register_courses(roll_number, courses)

        elif choice == '3':
            roll_number = int(input("Enter student roll number: "))
            grades = input("Enter grades for the courses (comma separated): ").split(",")
            system.enter_grades(roll_number, grades)

        elif choice == '4':
            roll_number = int(input("Enter student roll number: "))
            system.generate_grade_sheet(roll_number)

        elif choice == '5':
            item_id = int(input("Enter item ID: "))
            name = input("Enter item name: ")
            location = input("Enter item location: ")
            system.add_inventory_item(item_id, name, location)

        elif choice == '6':
            item_id = int(input("Enter item ID: "))
            new_location = input("Enter new item location: ")
            system.update_inventory_item(item_id, new_location)

        elif choice == '7':
            system.display_inventory()

        elif choice == '8':
            amount = float(input("Enter income amount: "))
            system.record_income(amount)

        elif choice == '9':
            amount = float(input("Enter expenditure amount: "))
            system.record_expenditure(amount)

        elif choice == '10':
            system.generate_account_summary()

        elif choice == '11':
            project_id = input("Enter project ID: ")
            title = input("Enter project title: ")
            description = input("Enter project description: ")
            system.add_research_project(project_id, title, description)

        elif choice == '12':
            faculty_name = input("Enter faculty name: ")
            publication_title = input("Enter publication title: ")
            year = input("Enter publication year: ")
            system.add_publication(faculty_name, publication_title, year)

        elif choice == '13':
            roll_number = int(input("Enter student roll number: "))
            system.query_student(roll_number)

        elif choice == '14':
            system.query_financials()

        elif choice == '0':
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
