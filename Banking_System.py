class BankAccount:
    """
    BankAccount class represents a basic bank account
    
    Attributes:
        name (str): Account holder name
        account_number (float): Unique account number
        __pin (int): Private PIN for authentication
        __balance (float): Private variable storing account balance
        transactions (list): Stores transaction history
    """
    def __init__(self, name, account_number, pin):
        """
        Constructor to initialize account details.

        Parameters:
            name (str): Name of the account holder
            account_number (str): Account number
            pin (int): Security PIN for the account
        """
        self.name = name
        self.account_number = account_number
        self.__pin = pin 
        self.__balance = 0
        self.transactions =[]

    # PIN authentication
    def authenticate(self):
        """
        Authenticates the user by checking the entered PIN.

        Returns:
            bool: True if PIN is correct, otherwise False
        """

        entered_pin = int(input("Enter PIN: "))
        return entered_pin == self.__pin
    
    # Deposit money
    def deposit(self, amount):
        """
        Deposits money into the account.

        Parameters:
            amount (float): Amount to deposit
        """
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    # Withdraw money
    def withdraw(self, amount):
        """
        Withdraws money from the account.

        Parameters:
            amount (float): Amount to withdraw
        """
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful")

    # Check balance
    def check_balance(self):
        """
        Displays the current account balance.
        """
        print("Current Balance:", self.__balance)

    # Transaction history
    def show_transactions(self):
        """
        Displays the list of all transactions.
        """
        print("\nTransaction History:")
        for t in self.transactions:
            print(t)

# Inheritance (Saving Account)
class SavingAccount(BankAccount):
    """
    SavingAccount class inherits from BankAccount.

    Additional Feature:
        interest_rate (float): Interest applied to the balance
    """

    def __init__(self, name, account_number, pin, interest_rate):
        """
        Initializes saving account details.

        Parameters:
            interest_rate (float): Interest percentage
        """
        super().__init__(name, account_number, pin)
        self.interest_rate = interest_rate

    def add_interest(self):
        """
        Adds interest to the current balance.
        """
        interest = self._BankAccount__balance * self.interest_rate / 100
        self._BankAccount__balance += interest
        print("Interest added:", interest)


# Main Program

"""
Main program that interacts with the user
and performs banking operations.
"""

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
pin = int(input("Create PIN: "))

account = SavingAccount(name, account_number, pin, 5)

while True:

    print("\n1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.Transaction History")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 2:
        if account.authenticate():
            amount = float(input("Enter amount: "))
            account.deposit(amount)

    elif choice == 3:
        if account.authenticate():
            amount = float(input("Enter amount: "))
            account.withdraw(amount)

    elif choice == 4:
        if account.authenticate():
            account.check_balance()

    elif choice == 5:
        if account.authenticate():
            account.show_transactions()

    elif choice == 6:
        print("Thank you for using the banking system")
        break

    else:
        print("Invalid option")   
