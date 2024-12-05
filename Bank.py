class Account:
    def __init__(self, account_holder, initial_balance, account_pin):
        self.account_holder = account_holder
        self.account_balance = initial_balance
        self.account_pin = account_pin

    def check_balance(self):
        return f"Current Balance: ₹{self.account_balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"₹{amount:.2f} deposited amount credited successfully."
        else:
            return "Deposit amount must be greater than 0."

    def withdraw(self, amount, pin):
        if self.validate_pin(pin):
            if amount <= self.account_balance:
                self.account_balance -= amount
                return f"₹{amount:.2f} withdrawn successfully."
            else:
                return "Insufficient funds."
        else:
            return "Invalid PIN "

    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin):
            if len(new_pin) == 4 and new_pin.isdigit():
                self.account_pin = new_pin
                return "PIN changed successfully."
            else:
                return "New PIN must 4-digit number."
        else:
            return "Old PIN is incorrect. PIN change failed."

    def validate_pin(self, pin):
        return self.account_pin == pin

def atm_menu(account):
    while True:
        print("ATM ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(account.check_balance())
        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            if amount.replace('.', '', 1).isdigit() and amount.count('.') < 2:
                amount = float(amount)
                print(account.deposit(amount))
            else:
                print("Invalid amount. Please enter a valid number.")
        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            if amount.replace('.', '', 1).isdigit() and amount.count('.') < 2:
                amount = float(amount)
                pin = input("Enter PIN: ")
                print(account.withdraw(amount, pin))
            else:
                print("Invalid amount. Please enter a valid number.")
        elif choice == "4":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(account.change_pin(old_pin, new_pin))
        elif choice == "5":
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main():

    account1 = Account("Ram", 2000.00, "1111")
    account2 = Account("Aaryan", 1000.00, "2222")

    print("Welcome to the ATM System\n")
    
    print("--- Ram's ATM ---")
    atm_menu(account1)

    print("\n--- Aaryan's ATM ---")
    atm_menu(account2)


if __name__ == "__main__":
    main()
