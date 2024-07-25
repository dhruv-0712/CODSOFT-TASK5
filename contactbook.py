contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact = {
        "phone_number": phone_number,
        "email": email,
        "address": address
    }

    contacts[name] = contact
    print("Contact added successfully!")

def view_contact_list():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, contact in contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("--------------------")

def search_contact():
    search_term = input("Enter contact name or phone number to search: ")
    found_contacts = []

    for name, contact in contacts.items():
        if search_term.lower() in name.lower() or search_term in contact["phone_number"]:
            found_contacts.append((name, contact))

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for name, contact in found_contacts:
            print(f"Name: {name}")
            print(f"Phone Number: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("--------------------")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print("Enter new contact details:")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")

        contact = {
            "phone_number": phone_number,
            "email": email,
            "address": address
        }

        contacts[name] = contact
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def contact_book():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")

contact_book()