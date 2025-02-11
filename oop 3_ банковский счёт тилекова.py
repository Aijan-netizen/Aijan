from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: {self.amount}"

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= amount

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder}, Balance: {self.balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

def main():
    account_number = int(input("Enter account number: "))
    account_holder = input("Enter account holder name: ")
    account = PersonalAccount(account_number, account_holder)
    
    while True:
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print("Current Balance:", account.get_balance())
        elif choice == "4":
            account.print_transaction_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please, try again.")

if __name__ == "__main__":
    main()