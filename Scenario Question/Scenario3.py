class InsufficientFundsError(Exception):
    pass

class BankAccount:
    """Base class for bank accounts."""

    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError("Insufficient funds.")

    def calculate_interest(self):
        pass

    def deduct_transaction_fee(self):
        pass

class SavingsAccount(BankAccount):
    """Subclass for savings accounts."""

    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, "Savings", balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class CheckingAccount(BankAccount):
    """Subclass for checking accounts."""

    def __init__(self, account_number, account_holder_name, balance, transaction_fee):
        super().__init__(account_number, account_holder_name, "Checking", balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self.balance -= self.transaction_fee

class BankCustomer:
    """Class to manage customer accounts."""

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        return None

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        account.withdraw(amount)

    def calculate_interest(self, account_number):
        account = self.get_account(account_number)
        account.calculate_interest()

    def deduct_transaction_fee(self, account_number):
        account = self.get_account(account_number)
        account.deduct_transaction_fee()

def menu():
    print("Welcome to the Bank Account Management System")
    print("1. Create a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Calculate interest")
    print("5. Deduct transaction fee")
    print("6. Quit")

    choice = input("Enter your choice: ")

    return choice

def main():
    customer = BankCustomer("John Doe", "123 Main Street", "123-456-7890")

    while True:
        choice = menu()

        if choice == "1":
            account_type = input("Enter the account type (Savings or Checking): ")

            if account_type == "Savings":
                interest_rate = float(input("Enter the interest rate: "))
                account = SavingsAccount(customer.name, customer.address, customer.phone_number, interest_rate)
            elif account_type == "Checking":
                transaction_fee = float(input("Enter the transaction fee: "))
                account = CheckingAccount(customer.name, customer.address, customer.phone_number, transaction_fee)
            else:
                print("Invalid account type.")
                continue

            customer.add_account(account)
            print("Account created successfully.")

        elif choice == "2":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the amount to deposit: "))

            customer.deposit(account_number, amount)
            print("Deposit successful.")

        elif choice == "3":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the amount to withdraw: "))

            try:
                customer.withdraw(account_number, amount)
                print("Withdrawal successful.")
            except InsufficientFundsError as e:
                print(f"Error: {e}")

        elif choice == "4":
            account_number = input("Enter the account number: ")

            customer.calculate_interest(account_number)
            print("Interest calculated successfully.")

        elif choice == "5":
            account_number = input("Enter the account number: ")

            customer.deduct_transaction_fee(account_number)
            print("Transaction fee deducted successfully.")

        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
