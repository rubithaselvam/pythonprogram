from random import choice

from mahil.learn.practice.contactbook import contact

contact = {}

def add_contact(name,phone,email):
    contact[name] = {"phone": phone, "email": email} # the colon is mistake
    print(f"contact name: {name} added successfully.")

def view_contact():
    if not contact:
        print("contact can not be founded.")

    else:
        print("\n contact details:")
        for name,details in contact.items():
            print(f"contact name: {name}, phone: {details['phone']}, email: {details['email']}")
        print()

def search_contact(name, phone,email): # phone email not given by me
    if name in contact:
        details = contact[name]
        print(f"contact name: {name}, phone: {phone}, email: {email}") # here i gave a details like phone: {details['phone']
        print()

    else:
        print("contact can not be founded.")

def update_contact(name, phone: None, email: None):
    if name  in contact:
        if phone:
            contact [name]["phone"] : phone
        if email:
            contact [name]["email"] : email
            print(f"contact name: {name} updated successfully.")
    else:
        print("contact can not be founded.")

def delete_contact(name):
    details = contact[name]
    print(f"contact name: {name} deleted successfully.")

def main():

    while True:

        print("\n contact details list:")

        print("1. add contact:")
        print("2. view contact:")
        print("3. search contact:")
        print("4. update contact:")
        print("5. delete contact:")
        print("6. exit")

        choice = input("enter your choice: ")

        if choice == '1':

            name = input("enter your name: ")
            phone = input("enter your number: ")
            email = input("enter your email: ")
            add_contact(name,phone,email)

        elif choice == '2':
            view_contact()

        elif choice == '3':

            name = input("enter your name: ")
            search_contact(name,phone,email)

        elif choice == '4':

            name = input("enter your name: ")
            phone = input("enter your number(or press enter key to skip): ")
            email = input("enter your email(or press enter key to skip): ")
            update_contact(name,phone if phone else None, email if email else None)

        elif choice == '5':

            name = input("enter your name: ")
            delete_contact(name)

        elif choice == '6':

            print("exit the contact details, have a wonderful day.")
            break

        else:
            print("invalid contact, try again")

if __name__ == "__main__":
    main()







