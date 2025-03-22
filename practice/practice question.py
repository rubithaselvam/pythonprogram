# Simple Contact Book Program

# Dictionary to store contacts
contacts = {}

def add_contact(name, phone, email):
    """Add a new contact."""
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} added successfully.")

def view_contacts():
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
        print()

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        details = contacts[name]
        print(f"Found Contact - Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print(f"Contact {name} not found.")

def update_contact(name, phone=None, email=None):
    """Update an existing contact."""
    if name in contacts:
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    """Delete a contact."""
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")
# above the function are did not get output
def main():
    """Main function to handle user input."""
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__": # this line only run the entire program
    main()