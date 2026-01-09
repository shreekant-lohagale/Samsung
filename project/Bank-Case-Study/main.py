from bank_system import BankManager
import sys

bank = BankManager()

print("-" * 5, "Welcome to the ABC Bank", "-" * 5)

while True:
    print("\n--- MAIN MENU ---")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")
    
    main_choice = input("Choose an option: ")

    if main_choice == '1':
        try:
            user_acc = int(input("Enter Account Number: "))
            user_pin = int(input("Enter PIN: "))
            
            if bank.verify_login(user_acc, user_pin):
                print(f"Login Successful. Welcome!")
                
                while True:
                    print("\n[Transaction Menu]")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    
                    sub_choice = input("Select: ")
                    
                    if sub_choice == '1':
                        amt = int(input("Amount to DEPOSIT: "))
                        success, msg = bank.deposit(user_acc, amt)
                        if success:
                            print(f"Deposited. New Balance: ₹{msg}")
                        else:
                            print(f"Error: {msg}")

                    elif sub_choice == '2':
                        amt = int(input("Amount to WITHDRAW: "))
                        success, msg = bank.withdraw(user_acc, amt)
                        if success:
                            print(f"Withdrawn. New Balance: ₹{msg}")
                        else:
                            print(f"Transaction Failed: {msg}") 
                            
                    elif sub_choice == '3':
                        bal = bank.get_balance(user_acc)
                        print(f"Current Balance: ₹{bal}")
                        
                    elif sub_choice == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Access Denied: Invalid Account Number or PIN.")
                
        except ValueError:
            print("Error: Please enter numeric values.")

    elif main_choice == '2':
        try:
            new_acc = int(input("Enter New Account Number: "))
            new_name = input("Enter Name: ")
            new_pin = int(input("Set PIN: "))
            start_bal = int(input("Initial Deposit: "))
            
            success, msg = bank.create_account(new_acc, new_name, new_pin, start_bal)
            print(msg)
        except ValueError:
            print("Error: Invalid input format.")

    elif main_choice == '3':
        print("Thank you for banking with us.")
        break 
    
    else:
        print("Invalid selection.")