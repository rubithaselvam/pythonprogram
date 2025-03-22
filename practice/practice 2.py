# from random import choice

contact = {}

def add_contact(name,phone,email):
     contact[name] = {"phone": phone, "email": email}
     print(f"contact name :{name} added successfully.")

def view_contact():
    if not contact:
        print("no contact founded.")
    else:
        print("\n contact list:")
        for name, details in contact.items():
            print(f"name: {name}, phone: {details['phone']}, email: {details['email']}")
        print()

def search_contact(name):
    if name in contact: # condition check
        details = contact[name]
        print(f"founded contact: {name}, phone: {details['phone']}, email: {details['email']}")
    else:
        print("no contact founded.")

def update_contact(name,phone: None,email: None):
    if name in contact:
        if phone:
            contact[name]["phone"] = phone
        if email:
            contact[name]["email"] = email
            print(f"contact name: {name} updated successfully.")
        else:
            print("no contact founded.")

def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"contact name: {name} deleted successfully")
    else:
        print("no contact founded")

def main():

    while True:
        print("\ncontact of book menu")

        print("1.add contacts")
        print("2.view contact")
        print("3.search contact")
        print("4.update contact")
        print("5.delete contact")
        print("6.exit")

        choice = input("enter your choice:")

        if choice == '1':
            name = input("enter your name:")
            phone = input("enter your phone number:")
            email = input("enter your email:")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contact()

        elif choice == '3':
            name = input("enter your name:")
            search_contact(name)

        elif choice == '4':
            name = input("update a name:")
            phone = input("enter a phone number(or press enter key to skip):")
            email = input("enter a email(or press enter key to skip):")
            update_contact(name, phone if phone else  None, email if email else None)

        elif choice == '5':
            name = input("enter your name:")
            delete_contact(name)

        elif choice == '6':
            print("exit the contact book menu, have a great day!")
            break

        else:
            print("invalid choice, please try again")

if __name__ == "__main__":
    main()
