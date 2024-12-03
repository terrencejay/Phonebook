def import_contacts():
     try:
         with open("contacts.txt", "r") as file:
             lines = file.readlines()
             current_contact = {}
             for line in lines:
                 #strip space
                 line = line.strip()
                 #if the line in the contact.txt file starts with 'Name' import the file
                 if line.startswith("Name:"):
                     if current_contact:
                         user_phonebook[current_contact['name']] = {
                             'Phone_number': current_contact['phone_number'],
                             'email': current_contact['email']
                         }
                     current_contact = {'name': line.split("Name: ")[1]}
                 elif line.startswith("Phone Number:"):
                     current_contact['phone_number'] = line.split("Phone Number: ")[1]
                 elif line.startswith("Email:"):
                     current_contact['email'] = line.split("Email: ")[1]
                 elif line == "-" * 20:
                     continue
             if current_contact:
                 user_phonebook[current_contact['name']] = {
                     'Phone_number': current_contact['phone_number'],
                     'email': current_contact['email']
                 }
             print("Contacts have been successfully imported from 'contacts.txt'.")
     except FileNotFoundError:
         print("The file 'contacts.txt' does not exist.")
     except Exception as e:
         print(f"An error occurred while reading the file: {e}")
