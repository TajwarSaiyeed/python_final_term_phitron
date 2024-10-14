from bank import Bank
from users import User

bank = Bank("Chittagong Bank")

def admin_user():
    while True:
        print(f"\nWelcome Admin! {bank.name}")
        print("Admin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Bankrupt")
        print("8. Exit Admin Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            user = bank.admin.create_account(name, email, address, account_type)
            print(f"Account created for {user.name}. Account Number: {user.account_number}")
            
            
        elif choice == "2":
            user_name = input("Enter the name of the user to delete: ")
            user = bank.find_user(user_name)
            if user:
                bank.admin.delete_account(user)
            else :
                print("Account does not exist")
                
                
        elif choice == "3":
            bank.admin.all_users()
            
            
        elif choice == "4":
            print(f"Total Bank Balance: {bank.total_balance}")
            
            
        elif choice == "5":
            print(f"Total Loan Amount: {bank.total_loans}")
            
            
        elif choice == "6":
            bank.loan_active = not bank.loan_active
            if bank.loan_active:
                print("Loan feature is now active")
            else:
                print("Loan feature is now inactive")
                
                
        elif choice == "7":
            bank.is_bankrupt = True
            print("The bank is now bankrupt!")
            
            
        elif choice == "8":
            break
        
        
        else:
            print("Invalid choice! Please try again.")
        


def user_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    account_type = input("Enter account type (Savings/Current): ")
    user = User(name, email, address, account_type)
    bank.users[user.account_number] = user
    print(f"Account created for {user.name}. Account Number: {user.account_number}")
    
    
    while True:
        print(f"\nWelcome Admin! {bank.name}")
        print("User Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer")
        print("7. Exit User Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = int(input("Enter amount to deposit: "))
            print(user.deposit(amount, bank))
            
            
        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            print(user.withdraw(amount, bank))
            
            
            
        elif choice == "3":
            print(f"Balance: {user.check_balance()}")
            
            
        elif choice == "4":
            print("Transaction History:\n")
            for transaction in user.check_transaction_history():
                print(transaction)
                
                
        elif choice == "5":
            if bank.loan_active == False:
                print("Loan feature is inactive")
                continue
            amount = int(input("Enter loan amount: "))
            print(user.take_loan(amount, bank))
            
            
        elif choice == "6":
            recipient_name = input("Enter recipient's name: ")
            amount = int(input("Enter transfer amount: "))
            print(user.transfer_tk(amount, recipient_name, bank))
            
            
        elif choice == "7":
            break
        
        
        else:
            print("Invalid choice! Please try again.")


while True:
    print(f"Welcome Admin! {bank.name}")
    print("\nMain Menu:")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    1
    if choice == "1":
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        
        if name == "admin" and password == "admin":
            admin_user()
        else :
            print("Invalid credentials")
    elif choice == "2":
        user_menu()
    elif choice == "3":
        break
    else:
        print("Invalid choice! Please try again.")