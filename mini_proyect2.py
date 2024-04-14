contacts = {}

def add_contact():
    name = input("Please introduce the name: ")
    number = input("Please introduce the phone number: ")
    email = input("Please introduce the email address: ")
    birthday= input("Please introduce the birthday")
    additional_info = input("Please introduce additional information (e.g., address, notes): ")
    contacts[name] = {"Phone Number": number, "Email Address": email, "Additional Information": additional_info, "Birthday":birthday}

def view_contacts():
    print("Here is the list of your contacts!")
    for name, details in contacts.items():
        print(f"Name: {name}")
        for key, value in details.items():
            print(f"{key}: {value}")
        print()

def delete_contact():
    name = input("What contact do you want to delete? ")
    if name in contacts:
        del contacts[name]
        print(f"The contact {name} has been deleted.")
    else:
        print("The contact does not exist.")

def search_contact():
    name = input("Enter the name of the contact you want to search for: ")
    if name in contacts:
        print(f"Name: {name}")
        for key, value in contacts[name].items():
            print(f"{key}: {value}")
    else:
        print("The contact does not exist.")

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print("Current Details:")
        for key, value in contacts[name].items():
            print(f"{key}: {value}")
        print("Please introduce the new details.")
        number = input("Please introduce the new phone number: ")
        email = input("Please introduce the new email address: ")
        additional_info = input("Please introduce the new additional information (e.g., address, notes): ")
        contacts[name] = {"Phone Number": number, "Email Address": email, "Additional Information": additional_info}
        print(f"The contact {name} has been updated.")
    else:
        print("The contact does not exist.")

def export_contacts():
    with open('contacts.txt', 'w') as f:
        for name, details in contacts.items():
            f.write(f"Name: {name}\n")
            for key, value in details.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")
    print("Contacts have been exported to contacts.txt")

def import_contacts():
    with open('contacts.txt', 'r') as f:
        lines = f.readlines()
        name = ""
        for line in lines:
            if line.strip() != "":
                key, value = line.strip().split(": ")
                if key == "Name":
                    name = value
                else:
                    if name not in contacts:
                        contacts[name] = {}
                    contacts[name][key] = value
    print("Contacts have been imported from contacts.txt")

while True:
    interface = input('''
    1) Add a new contact
    2) View all contacts
    3) Delete a contact
    4) Edit a contact
    5) Search for a contact
    6) Export contacts
    7) Import contacts
    8) Quit
    ''')

    if interface == "1":
        add_contact()
    elif interface == "2":
        view_contacts()
    elif interface == "3":
        delete_contact()
    elif interface == "4":
        edit_contact()
    elif interface == "5":
        search_contact()
    elif interface == "6":
        export_contacts()
    elif interface == "7":
        import_contacts()
    elif interface == "8":
        print("Goodbye!")
        export_contacts()
        print("Your contacts are autosaved")
        break
