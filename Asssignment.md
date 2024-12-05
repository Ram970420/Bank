# **Assignment: ATM Machine Simulation**

---

## **Objective**

Build a Python program that simulates an **ATM Machine**. The system should allow a user to interact with an account to perform operations such as checking balance, depositing money, withdrawing money, and changing their PIN.

This assignment will help you practice:

1. **Variables and Data Types**
2. **Input and Output**
3. **Functions**: Parameterized, void, and return-type methods.
4. **Classes and Objects**

---

## **Problem Statement**

Design and implement a Python program that includes:

1. **An Account Class**:
   - Attributes:
     - `account_holder` (string): Name of the account holder.
     - `account_balance` (float): Current account balance.
     - `account_pin` (string): 4-digit PIN for account security.
   - Methods:
     - `check_balance()` (return type): Returns the current balance.
     - `deposit(amount)` (void method): Adds the amount to the account balance.
     - `withdraw(amount, pin)` (void method): Deducts the amount from the balance if the PIN is correct.
     - `change_pin(old_pin, new_pin)` (void method): Changes the account PIN if the old PIN is correct.
     - `validate_pin(pin)` (return type): Validates the provided PIN and returns `True` or `False`.

2. **Interactive Menu**:
   - Options:
     1. Check account balance.
     2. Deposit money.
     3. Withdraw money.
     4. Change PIN.
     5. Exit the program.

3. **Features**:
   - Use **input()** to get user input for account operations.
   - Use variables and data types effectively for storing and manipulating data.
   - Provide meaningful prompts and messages for user interaction.

---

## **Assignment Tasks**

1. **Define the Account Class**:
   - Create the class with appropriate attributes and methods.
   - Implement methods to perform the specified operations.

2. **Enhance the Menu**:
   - Add a menu-driven system to let users perform multiple operations in one session.
   - Handle invalid inputs gracefully with error messages.

3. **Test the System**:
   - Create at least two accounts and perform all operations on both accounts.
   - Display a summary of each operation after it is performed.

4. **Add Extra Features (Optional)**:
   - Allow the user to view account details (except the PIN).
   - Prevent PIN changes unless the new PIN is a valid 4-digit number.
   - Implement error handling for insufficient funds during withdrawals.

---

## **Sample Output**

Below is an example of how your program should behave:

--- ATM Machine ---

Check Balance
Deposit Money
Withdraw Money
Change PIN
Exit Enter your choice: 1 Current Balance: $1000.00
--- ATM Machine ---

Check Balance
Deposit Money
Withdraw Money
Change PIN
Exit Enter your choice: 2 Enter amount to deposit: 200 $200.00 deposited successfully.
--- ATM Machine ---

Check Balance
Deposit Money
Withdraw Money
Change PIN
Exit Enter your choice: 5 Thank you for using the ATM. Goodbye!

