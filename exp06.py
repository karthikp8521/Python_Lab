class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        if balance >= 0:
            self.balance = balance
        else:
            self.balance = 0
            print("Invalid initial balance! Set to 0.")

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.balance += amount
            print("Deposited:", amount)

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    # Balance check
    def check_balance(self):
        print("Current Balance:", self.balance)


# Main Program
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

acc = BankAccount(name, balance)

while True:
    print("\n1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = float(input("Enter deposit amount: "))
        acc.deposit(amt)

    elif choice == 2:
        amt = float(input("Enter withdrawal amount: "))
        acc.withdraw(amt)

    elif choice == 3:
        acc.check_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")