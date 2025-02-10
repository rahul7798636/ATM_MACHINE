class Account:
    def __init__(self, account_no, pin, balance, account_type):
        self.account_no = account_no  
        self.pin = pin 
        self.balance = balance  
        self.account_type = account_type  # Account type ("privileged" or "normal")


class ATM:
    def __init__(self):
        self.customers = {}  # Dictionary to store Account objects by account number
        self.atm_cash = 100000  # ATM's cash balance 

    def add_customer(self, account):
        
        if account.account_no not in self.customers:
            self.customers[account.account_no] = account  
            print(f'Customer with account_no {account.account_no} added.')
        else:
            print('Account already exists.')

    def add_account(self):
        
        account_no = int(input('Enter the account_no you want to add: '))
        pin = int(input('Enter your pin: '))
        balance = float(input('Enter the amount you want to add: '))
        account_type = input('Enter your account_type (privileged/normal): ').lower()

        account = Account(account_no, pin, balance, account_type)

        self.add_customer(account)  # Adds the new account to the ATM system

    def authenticate(self, account_no, pin):
        
        if account_no in self.customers:
            account = self.customers[account_no]  
            if account.pin == pin:
                return account  # Authentication successful
            else:
                print('Incorrect pin.')
        else:
            print('Account not found.')
        

    def withdraw(self):
        
        if self.atm_cash <= 0:
            print("ATM is out of service. No cash available.")
            
        account_no = int(input('Enter your account no: '))
        pin = int(input('Enter your pin: '))
        amount = float(input('Enter amount to withdraw: '))

        account = self.authenticate(account_no, pin)  # Authenticate user
        
        if account:  # If the user is authenticated
            
            if self.atm_cash >= amount:
                
                if account.account_type == 'privileged' :
                    fee = 5
                else:
                    fee = 10
                total_deduction = amount + fee

                if account.balance >= total_deduction:
                    account.balance -= total_deduction  
                    self.atm_cash -= amount  
                    print(f'Withdrawal successful. Your new balance is {account.balance}.')
                else:
                    print('Insufficient balance. ')
            else:
                print('Insufficient cash in ATM.')
        else:
            print('Authentication failed. Cannot withdraw.')

    def deposit(self):
        
        account_no = int(input('Enter your account_no: '))
        pin = int(input('Enter your pin: '))
        amount = float(input('Enter the amount you want to deposit: '))

        account = self.authenticate(account_no, pin)  # Authenticate user
        
        if account:
            account.balance += amount  
            self.atm_cash += amount  
            print(f'Deposit successful. Your new balance is {account.balance}.')
        else:
            print('Authentication failed. Deposit canceled.')

    def check_balance(self):
        
        account_no = int(input('Enter your account_no: '))
        pin = int(input('Enter your pin: '))

        account = self.authenticate(account_no, pin)  # Authenticate user
        
        if account:
            print(f'Your current balance is {account.balance}.')
        else:
            print('Authentication failed. Balance check canceled.')


# ATM object
atm = ATM()

# Test accounts
acc1 = Account(1234, 9999, 5000, 'privileged')
acc2 = Account(5678, 8888, 4000, 'normal')

# Add customers to the ATM system
atm.add_customer(acc1)
atm.add_customer(acc2)

# Uncomment the below to perform different transactions 

# " Test ATM functionality "

# atm.add_account()
# atm.withdraw()  
# atm.deposit()  
# atm.check_balance() 
git --version
git init

