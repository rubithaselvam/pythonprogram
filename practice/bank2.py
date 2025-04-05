# custom exception for insufficient funds
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for this withdrawal"):
        super().__init__(message)

# bank account class
class BankAccount:
    def __init__(self,account_number, balance=0):
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.account = account_number
        self.balance = balance
        print(f"account number: {account_number}, bank account: {balance}") # key-value

    def deposits(self,amount):
        if amount <=0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount
        print(f"account number: {self.account}, deposit: {amount}, new balance: {self.balance}")

    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(f"account number: {self.account}, cannot withdraw a {amount}. Available balance: {self.balance}")
        self.balance -= amount
        print(f"account number: {self.account}, withdrawn : {amount}, New Balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def close_account(self):
        print(f"{self.account} account closed successfully.")

accounts = {} # to store a lot of account

while True:
    print("\naccount details")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. close account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            print("Account already exists.")
        else:
            initial_balance = float(input("Enter initial balance: "))
            accounts[account_number] = BankAccount(account_number, initial_balance)

    elif choice == "2":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[account_number].deposits(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter withdrawal amount: "))
            try:
                accounts[account_number].withdrawal(amount)
            except InsufficientFundsError as e:
                print(e)
        else:
            print("Account not found.")

    elif choice == "4":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            print(f"Account number: {account_number}, Balance: {accounts[account_number].get_balance()}")
        else:
            print("Account not found.")

    elif choice == "5":
        account_number = input("enter account number to close: ")
        if account_number in accounts:
            print(f"account number: {account_number}, close: {accounts[account_number].close_account()}")
            del accounts[account_number]
        else:
            print("account not found")

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")