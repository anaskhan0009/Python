class Component:
    def __init__(self, name, component_type, language, keywords, category):
        """
        Initialize a software component.
        """
        self.name = name  # Component name
        self.component_type = component_type  # Design or Code
        self.language = language  # Language used (e.g., Python, UML, etc.)
        self.keywords = keywords  # List of keywords for search
        self.category = category  # Category for classification
        self.usage_count = 0  # Times used
        self.query_count = 0  # Times queried but not used

    def __str__(self):
        """
        String representation for display.
        """
        return (f"Name: {self.name}, Type: {self.component_type}, "
                f"Language: {self.language}, Keywords: {', '.join(self.keywords)}, "
                f"Category: {self.category}, Used: {self.usage_count}, Queried: {self.query_count}")


class ComponentCatalogue:
    def __init__(self):
        """
        Initialize an empty catalogue.
        """
        self.catalogue = []

    def add_component(self):
        """
        Add a new component to the catalogue.
        """
        name = input("Enter component name: ")
        component_type = input("Enter component type (Design/Code): ")
        language = input("Enter language or notation (e.g., Python, UML, ERD): ")
        keywords = input("Enter keywords (comma-separated): ").split(",")
        category = input("Enter category: ")
        self.catalogue.append(Component(name, component_type, language, [k.strip() for k in keywords], category))
        print(f"Component '{name}' added successfully!\n")

    def delete_component(self):
        """
        Delete a component by name.
        """
        name = input("Enter the component name to delete: ")
        for component in self.catalogue:
            if component.name == name:
                self.catalogue.remove(component)
                print(f"Component '{name}' deleted successfully!\n")
                return
        print(f"Component '{name}' not found!\n")

    def search_component(self):
        """
        Search components based on keywords.
        """
        query = input("Enter keywords for search (comma-separated): ").split(",")
        query = [q.strip().lower() for q in query]
        found = False

        for component in self.catalogue:
            if any(q in [k.lower() for k in component.keywords] for q in query):
                print(f"\nFound Component:\n{component}")
                use = input("Do you want to use this component? (yes/no): ").strip().lower()
                if use == "yes":
                    component.usage_count += 1
                    print(f"Component '{component.name}' marked as used.\n")
                else:
                    component.query_count += 1
                found = True

        if not found:
            print("No components found matching your keywords.\n")

    def browse_by_category(self):
        """
        Browse components by category.
        """
        categories = set(c.category for c in self.catalogue)
        print("Available Categories:")
        for category in categories:
            print(f"- {category}")

        selected_category = input("\nEnter category to browse: ").strip()
        print(f"\nComponents in Category '{selected_category}':")
        found = False
        for component in self.catalogue:
            if component.category.lower() == selected_category.lower():
                print(component)
                found = True
        if not found:
            print("No components found in this category.\n")

    def purge_unused_components(self):
        """
        Delete components with zero usage and high query count.
        """
        threshold = int(input("Enter the query threshold for purging: "))
        initial_count = len(self.catalogue)
        self.catalogue = [c for c in self.catalogue if not (c.usage_count == 0 and c.query_count >= threshold)]
        purged_count = initial_count - len(self.catalogue)
        print(f"{purged_count} components purged from the catalogue.\n")

    def display_all_components(self):
        """
        Display all components in the catalogue.
        """
        if not self.catalogue:
            print("No components in the catalogue.\n")
            return

        print("\nAll Components in Catalogue:")
        for component in self.catalogue:
            print(component)


def main():
    catalogue = ComponentCatalogue()

    while True:
        print("\n--- Software Component Catalogue ---")
        print("1. Add Component")
        print("2. Delete Component")
        print("3. Search Component")
        print("4. Browse by Category")
        print("5. Purge Unused Components")
        print("6. Display All Components")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            catalogue.add_component()
        elif choice == "2":
            catalogue.delete_component()
        elif choice == "3":
            catalogue.search_component()
        elif choice == "4":
            catalogue.browse_by_category()
        elif choice == "5":
            catalogue.purge_unused_components()
        elif choice == "6":
            catalogue.display_all_components()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
