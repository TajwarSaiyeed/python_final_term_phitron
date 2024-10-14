import random

class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = name +str(random.randint(1000, 9999))
        self.balance = 0
        self.loan = 0
        self.loan_count = 0
        self.transaction_history = []
        
    def deposit(self, amount, bank):
        if amount < 0:
            return "Invalid amount"
        self.balance += amount
        bank.total_balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        return f"Deposited: {amount}"
    
    def withdraw(self, amount, bank):
        if amount > self.balance:
            return "Withdrawal amount exceeded"
        if bank.is_bankrupt:
            return "The bank is bankrupt! Withdrawals are not possible."
        
        self.balance -= amount
        bank.total_balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")
        f"Withdrew: {amount}"
        return f"Withdrew: {amount}"

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount, bank):
        if self.loan_count >= 2:
            return "Loan limit exceeded"
        self.loan += amount
        bank.total_loans += amount
        self.balance += amount
        self.loan_count += 1
        self.transaction_history.append(f"Loan taken: {amount}")
        return f"Loan taken: {amount}"
        
    def transfer_tk(self, amount, recipient_name, bank):
        if bank.is_bankrupt:
            return "The bank is bankrupt! Transfers are not possible."
        if amount > self.balance:
            return "Withdrawal amount exceeded"
        
        user = bank.find_user(recipient_name)
        if user == None:
            return "Account does not exist"
        
        self.balance -= amount
        user.balance += amount
        self.transaction_history.append(f"Transferred: {amount} to {user.name}")
        return f"Transferred: {amount} to {user.name}"

class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.bank.users[user.account_number] = user
        return user
        

    def delete_account(self, user):
        self.bank.users.pop(user.account_number)
        print(f"Account deleted for {user.name}")

    def all_users(self):
        print("All Accounts:")
        print("Name\tEmail\tAddress\tAccount Type\tBalance")
        for value in self.bank.users.values():
            print(f"{value.name}\t{value.email}\t{value.address}\t{value.account_type}\t{value.balance}")
