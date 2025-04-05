expenses = {}
expense_id = 0

def add_expenses(amount, items, date, transportation, product):
    global expense_id
    expense_id += 1
    expenses[expense_id] = {"items":items, "amount": amount, "product": product, "date": date, "transportation": transportation} # EXPENSES[AMOUNT] = {"ITEMS": ITEMS}
    print(f"expenses {items} added successfully.")

def view_expenses():
        if not expenses:
            print("you didn't spend the amount on this item.")
        else:
            print("\ndetails of expenses.")
            for expense_id,details in expenses.items():
                print(f"expense_id: {expense_id}, items: {details['items']}, amount: {details['amount']}, product: {details['product']}, date: {details['date']}, transportation: {details['transportation']}")
            print()

def search_expenses(expense_id):
    if expense_id in expenses:
        details = expenses[expense_id]
        print(f"expense_id: {expense_id}, items: {details['items']}, amount: {details['amount']}, product: {details['product']}, date: {details['date']}, transportation: {details['transportation']}")
    else:
        print("item can not be founded.")

def update_expenses(expense_id, food = None,amount= None,date= None,transportation= None,product= None): # NONE KUDUKULA
    if expense_id in expenses:
        if amount:
            expenses[expense_id]["amount"] = amount
        if product:
            expenses[expense_id]["product"] = food
        if date:
            expenses[expense_id]["date"] = date
        if transportation:
            expenses[expense_id]["transportation"] = transportation
        print(f"expenses {expense_id} added successfully.") # IDENTATION WRONG
    else:
        print(f"expenses {expense_id} can not be found.")

def delete_expenses(expense_id):
    if expense_id in expenses:
        del expenses[expense_id]
        print(f"expenses {expense_id} deleted successfully.")
    else:
        print("items can not be found.")

def main():

    while True:
        print("\nexpenses of detail list:")
        print("1. Add expenses")
        print("2. View expenses")
        print("3. Search expenses")
        print("4. Update expenses")
        print("5. Delete expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            items = input("Enter a item name: ")
            product = input("Enter a product name: ")
            amount = input("Enter a amount: ")
            date = input("Enter a date: ")
            transportation = input("Enter a transportation: ")
            add_expenses(amount,items,date,transportation,product)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = int(input("Enter a number of id: "))
            search_expenses(expense_id)

        elif choice == '4':
            expense_id = int(input("Enter a number id to update: "))
            food = input("Enter a product name (or press a enter key to skip): ")
            amount = input("Enter a amount: ")
            date = input("Enter a date(or press a enter key to skip): ")
            transportation = input("Enter a transportation(or press a enter key to skip): ")
            update_expenses(expense_id, food if food else None, amount if amount else None, date if date else None, transportation if transportation else None,product if product else None) # ELSE KUDUKULA

        elif choice == "5":
            expense_id = int(input("Enter number to delete: "))
            delete_expenses(expense_id)

        elif choice  == "6":
            print("exit the expenses details list.")
            break
        else:
            print("Invalid choice please enter a valid choice")

if __name__ == "__main__":
    main()
