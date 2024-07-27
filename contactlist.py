#   CONTACT LIST

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append(Contact(name, phone, email, address))
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact.name} - {contact.phone}")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if query.lower() in contact.name.lower() or query in contact.phone]
    if results:
        for contact in results:
            print(contact)
    else:
        print("No contacts found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            new_name = input(f"Enter new name (leave blank to keep {contact.name}): ")
            new_phone = input(f"Enter new phone (leave blank to keep {contact.phone}): ")
            new_email = input(f"Enter new email (leave blank to keep {contact.email}): ")
            new_address = input(f"Enter new address (leave blank to keep {contact.address}): ")
            contact.update(new_name, new_phone, new_email, new_address)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = []
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
 