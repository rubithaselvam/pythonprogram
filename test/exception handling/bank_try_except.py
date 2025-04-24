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

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal amount mus be positive")
        if amount > self.balance:
            raise InsufficientFundsError(f"account number: {self.account}, cannot withdraw a {amount}."
                                         f" Available balance: {self.balance}")
        self.balance -= amount
        print(f"account number: {self.account}, withdrawn : {amount}, New Balance: {self.balance}")

    def get_balance(self):
        return self.balance
account = {}

try:
    account[1] = BankAccount(1,800)
    account[2] = BankAccount(2,700)
    account[3] = BankAccount(3,4000)

    print("==" * 36)

    account[1].deposits(900)
    account[2].deposits(100)
    account[3].deposits(800)


    print("==" * 36)

    account[1].withdraw(300)
    account[2].withdraw(900)
    account[3].withdraw(3000)

    print("==" * 36)

except ValueError as v:
    print(f"ValueError: {v}")
except InsufficientFundsError as i:
    print(f"InsufficientFundsError : {i}")



