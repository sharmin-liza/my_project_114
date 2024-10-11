import datetime

# User Class
class User:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []
        self.loan_taken = False

    def create_account(self):
        print(f"Account created successfully for {self.name}. Initial balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount} on {datetime.datetime.now()}")
        print(f"${amount} deposited successfully. Current balance: ${self.balance}")

    def withdraw(self, amount, bank):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount} on {datetime.datetime.now()}")
            print(f"${amount} withdrawn successfully. Current balance: ${self.balance}")
        elif bank.is_bankrupt(self.balance, amount):
            print("The bank is bankrupt. Unable to withdraw money.")
        else:
            print("Insufficient balance to withdraw.")

    def transfer(self, amount, recipient, bank):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.name} on {datetime.datetime.now()}")
            recipient.transaction_history.append(f"Received ${amount} from {self.name} on {datetime.datetime.now()}")
            print(f"${amount} transferred successfully to {recipient.name}.")
        elif bank.is_bankrupt(self.balance, amount):
            print("The bank is bankrupt. Unable to transfer money.")
        else:
            print("Insufficient balance to transfer.")

    def check_balance(self):
        print(f"Available balance for {self.name}: ${self.balance}")

    def check_transaction_history(self):
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print(f"Transaction history for {self.name}:")
            for transaction in self.transaction_history:
                print(transaction)

    def take_loan(self, bank):
        if not bank.loan_feature:
            print("Loan feature is currently disabled.")
        elif not self.loan_taken:
            loan_amount = 2 * self.balance
            bank.total_loan_amount += loan_amount
            self.balance += loan_amount
            self.loan_taken = True
            self.transaction_history.append(f"Loan of ${loan_amount} taken on {datetime.datetime.now()}")
            print(f"Loan of ${loan_amount} taken successfully. Current balance: ${self.balance}")
        else:
            print("Loan has already been taken.")

# Admin Class
class Admin:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def create_account(self, name, initial_balance=0):
        user = User(name, initial_balance)
        self.bank.add_user(user)
        user.create_account()
        return user

    def check_total_balance(self):
        print(f"Total available balance in the bank: ${self.bank.total_balance()}")

    def check_total_loan_amount(self):
        print(f"Total loan amount in the bank: ${self.bank.total_loan_amount}")

    def toggle_loan_feature(self, status):
        self.bank.loan_feature = status
        print(f"Loan feature has been {'enabled' if status else 'disabled'}.")

# Bank Class
class Bank:
    def __init__(self):
        self.users = []
        self.total_loan_amount = 0
        self.loan_feature = True

    def add_user(self, user):
        self.users.append(user)

    def total_balance(self):
        return sum(user.balance for user in self.users)

    def is_bankrupt(self, user_balance, withdraw_amount):
        if self.total_balance() - (withdraw_amount - user_balance) < 0:
            return True
        return False

# Main program
if __name__ == "__main__":
    # Create a bank
    bank = Bank()

    # Create admin
    admin = Admin("Bank Admin", bank)

    # Admin creates user accounts
    user1 = admin.create_account("Alice", 1000)
    user2 = admin.create_account("Bob", 500)

    # User operations
    user1.deposit(500)
    user1.withdraw(300, bank)
    user1.transfer(200, user2, bank)
    user1.check_balance()
    user1.check_transaction_history()

    # User taking a loan
    user1.take_loan(bank)

    # Admin operations
    admin.check_total_balance()
    admin.check_total_loan_amount()
    admin.toggle_loan_feature(False)  # Disable loan feature

    # Trying to take a loan after disabling the loan feature
    user2.take_loan(bank)
