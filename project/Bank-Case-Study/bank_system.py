# bank_system.py

class BankManager:
    def __init__(self):
        self.bank_db = {
            123456: {'name': 'Alice', 'pin': 1234, 'balance': 5000},
            987656: {'name': 'Bob',   'pin': 9876, 'balance': 10000}
        }

    def verify_login(self, acc_num, pin):
        if acc_num in self.bank_db and self.bank_db[acc_num]['pin'] == pin:
            return True
        return False

    def create_account(self, acc_num, name, pin, initial_deposit):
        if acc_num in self.bank_db:
            return False, "Account number already exists!"
        
        self.bank_db[acc_num] = {
            'name': name,
            'pin': pin,
            'balance': initial_deposit
        }
        return True, "Account created successfully."

    def get_balance(self, acc_num):
        return self.bank_db[acc_num]['balance']

    def deposit(self, acc_num, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        
        self.bank_db[acc_num]['balance'] += amount
        return True, self.bank_db[acc_num]['balance']

    def withdraw(self, acc_num, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        
        current_bal = self.bank_db[acc_num]['balance']
        
        # CRITICAL FIX: Overdraft Protection
        if current_bal >= amount:
            self.bank_db[acc_num]['balance'] -= amount
            return True, self.bank_db[acc_num]['balance']
        else:
            return False, "Insufficient funds."