contacts = {}
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        phone = input("Enter phone number: ")
        if phone in contacts:
            print("Contact already exists!")
        else:
            name = input("Enter contact name: ")
            contacts[phone] = name
            print("Contact added successfully!")
    elif choice == "2":
        phone = input("Enter phone number to search: ")
        if phone in contacts:
            print("Name:", contacts[phone])
        else:
            print("Contact not found!")
    elif choice == "3":
        phone = input("Enter phone number to update: ")
        if phone in contacts:
            name = input("Enter new name: ")
            contacts[phone] = name
            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    elif choice == "4":
        phone = input("Enter phone number to delete: ")
        if phone in contacts:
            del contacts[phone]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    elif choice == "5":
        if len(contacts) == 0:
            print("Contact book is empty!")
        else:
            print("\nContacts:")
            for phone, name in contacts.items():
                print("Phone:", phone, "Name:", name)
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please try again.")


        
