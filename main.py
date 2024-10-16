import json

# File where contacts will be stored
CONTACTS_FILE = "contacts.json"

# Load contacts from file or create an empty dictionary if file doesn't exist
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    if name in contacts:
        print("Contact already exists. Use edit to update the contact.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

# Main menu
def menu():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact management system
if __name__ == "__main__":
    menu()
