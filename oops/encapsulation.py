class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder # public
        self.account_type = "CURRENT" # protected
        self.__balance = balance # private

    def deposit(self,deposit_amount,balance = 3000):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            print(f"{deposit_amount} amount is added successfully, new balance: {self.__balance}")
        else:
            print(f"{balance}the amount did not deposited")

    def withdraw(self,withdraw_amount):
        if 0 < withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
            print(f"{withdraw_amount} amount is with drawed successfully")
        else:
            print(f"Insufficient amount please withdraw tha amount less than of your account {self.__balance}")

    def get_balance(self):
        return self.__balance

    def get_holder(self):
        return self.account_holder

    def get_type(self):
        return self.account_type

account = BankAccount("RUBITHA",3000)
print("account holder: ",account.get_holder())
print("account type: ", account.get_type())
account.deposit(2000)
account.withdraw(1000)
print("balance amount: ",account.get_balance())




