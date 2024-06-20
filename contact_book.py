class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def update_contact(self, name, new_phone_number, new_email):
        contact = self.search_contact(name)
        if contact:
            contact.phone_number = new_phone_number
            contact.email = new_email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\n==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
            print(f"Contact '{name}' added successfully.")
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            name = input("Enter name to search: ")
            found_contact = contact_book.search_contact(name)
            if found_contact:
                print(f"Contact found - Name: {found_contact.name}, Phone: {found_contact.phone_number}, Email: {found_contact.email}")
            else:
                print(f"Contact '{name}' not found.")
        
        elif choice == '4':
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contact_book.update_contact(name, new_phone_number, new_email)
        
        elif choice == '5':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
