# Bank Acc with attritubes like account_number, balance, date_of_opening and customer_name and methods like deposit, withdraw and check_balance

from datetime import date

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = 0.0

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount>0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}")
            else:
                print("Insufficient funds for withdrawal")
        else:
            print("Withdrawal must be positive.")

    def check_balance(self):
        return self.balance

account = BankAccount("123", "Shreya", date(2024, 4, 22))

print(f"Initial balance: {account.check_balance()}")

account.deposit(100)

print(f"Balance after deposit: {account.check_balance()}")

account.withdraw(50)

print(f"Balance after withdrawal: {account.check_balance()}")


    