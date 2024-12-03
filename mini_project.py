import os

user_phonebook = {}

def main_menu():
    while True:
        try:
            first_choice = int(input(
                "What would you like to do? "
                "Add a new contact(1), Edit an existing contact(2), Delete a contact(3), "
                "Search for a contact(4), Display all contacts(5), Export contacts to a text file(6), "
                "Import contacts from a text file(7), Quit(8): "
            ))
            if first_choice == 1:
                add_contact()
            elif first_choice == 2:
                edit_contact()
            elif first_choice == 3:
                delete_contact()
            elif first_choice == 4:
                contact_search()
            elif first_choice == 5:
                display_contacts()
            elif first_choice == 6:
                export_contacts()
            elif first_choice == 7:
                import_contacts()
            elif first_choice == 8:
                print("Thanks for using our phonebook!")
                break
        except ValueError:
            print("Please enter an option between 1-8.")

def add_contact():
    try:
        new_first_name = input("Enter new first and last name: ")
        new_phone_number = input("Enter contact phone number: ")
        #make sure phone number is 10 digits
        if len(new_phone_number) != 10 or not new_phone_number.isdigit():
            raise ValueError("Phone number should be 10 digits.")
        new_email = input("What is the contact email? ")
        user_phonebook[new_first_name] = {
            'Phone_number': new_phone_number,
            'email': new_email
        }
        print(f"{new_first_name} added to phonebook.\n")
    except ValueError as e:
        print(e)

def edit_contact():
    if user_phonebook:
        for contact, info in user_phonebook.items():
            print(contact, info)
        contact_to_edit = input("Which contact would you like to edit? ")
        #if there is a contact, edit the selected contact
        if contact_to_edit in user_phonebook:
            new_number = input(f"What is the new number for {contact_to_edit}: ")
            new_email = input(f"What is the new email for {contact_to_edit}: ")
            user_phonebook[contact_to_edit] = {
                'Phone_number': new_number,
                'email': new_email
            }
            print(f"Contact {contact_to_edit} updated.")
        else:
            print(f"{contact_to_edit} not found.")
    else:
        print("The phonebook is empty.")

def delete_contact():
    if user_phonebook:
        for contact, info in user_phonebook.items():
            print(f"Name: {contact}\nPhone Number: {info['Phone_number']}, Email: {info['email']}")
        contact_to_del = input("Which contact would you like to delete? ")
        if contact_to_del in user_phonebook:
            del user_phonebook[contact_to_del]
            print(f"{contact_to_del} deleted.")
        else:
            print(f"{contact_to_del} not found.")
    else:
        print("Phonebook is empty.")

def contact_search():
    if user_phonebook:
        name_to_search = input("Who are you looking for? ")
        if name_to_search in user_phonebook:
            contact = user_phonebook[name_to_search]
            print(f"Name: {name_to_search}")
            print(f"Phone Number: {contact['Phone_number']}")
            print(f"Email: {contact['email']}")
        else:
            print(f"Contact '{name_to_search}' not found.")
    else:
        print("Phonebook is empty.")

def display_contacts():
    if user_phonebook:
        for name, info in user_phonebook.items():
            print(f"Name: {name}")
            print(f"Phone Number: {info['Phone_number']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("The phonebook is empty.")

def export_contacts():
    if user_phonebook:
        try:
            with open("contacts.txt", "w") as file:
                for name, info in user_phonebook.items():
                    file.write(f"Name: {name}\n")
                    file.write(f"Phone Number: {info['Phone_number']}\n")
                    file.write(f"Email: {info['email']}\n")
                    file.write("-" * 20 + "\n")
            print("Contacts have been successfully exported to 'contacts.txt'.")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
    else:
        print("The phonebook is empty. No contacts to export.")

main_menu()
