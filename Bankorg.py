class BankAccount:
    def __init__(self, account_number, holder_name, account_type, initial_balance=0.0):
        self.account_number = account_number
        self.holder = holder_name
        self.acc_type = account_type
        self._balance = initial_balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully into Account {self.account_number}.")
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully from Account {self.account_number}.")
            return True
        elif amount > self._balance:
            print("Transaction denied: Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")
        return False

    def get_balance(self):
        return self._balance


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def open_account(self):
        print("\n--- OPEN NEW ACCOUNT ---")
        name = input("Enter customer name: ").strip()
        acc_type = input("Enter account type (Savings/Current): ").strip()
        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative.")
                return
        except ValueError:
            print("Invalid currency input.")
            return

        acc_num = self.next_account_number
        # Create a new BankAccount instance and store it
        self.accounts[acc_num] = BankAccount(acc_num, name, acc_type, initial_deposit)
        print(f"Account successfully created! Assigned Account Number: {acc_num}")
        self.next_account_number += 1

    def _get_account(self, prompt="Enter account number: "):
        """Helper method to fetch an account object safely."""
        try:
            acc_num = int(input(prompt))
            if acc_num in self.accounts:
                return self.accounts[acc_num]
            print("Account record not found.")
        except ValueError:
            print("Invalid account format.")
        return None

    def deposit(self):
        print("\n--- DEPOSIT ---")
        account = self._get_account()
        if account:
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input.")

    def withdraw(self):
        print("\n--- WITHDRAW ---")
        account = self._get_account()
        if account:
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input.")

    def transfer(self):
        print("\n--- TRANSFER ---")
        print("Sender verification:")
        sender = self._get_account("Enter your account number (Sender): ")
        if not sender:
            return
        
        print("Receiver verification:")
        receiver = self._get_account("Enter recipient account number (Receiver): ")
        if not receiver:
            return

        if sender.account_number == receiver.account_number:
            print("Cannot transfer funds to the same account.")
            return

        try:
            amount = float(input("Enter amount to transfer: "))
            # Atomically deduct from sender and add to receiver if check passes
            if amount > 0 and sender.get_balance() >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Successfully transferred ₹{amount} to Account {receiver.account_number}.")
            else:
                print("Transfer failed. Check balance or input amount.")
        except ValueError:
            print("Invalid input.")

    def balance_inquiry(self):
        print("\n--- BALANCE ---")
        account = self._get_account()
        if account:
            print(f"Current Balance: ₹{account.get_balance()}")

    def mini_statement(self):
        print("\n--- MINI STATEMENT ---")
        account = self._get_account()
        if account:
            print(f"Account Holder: {account.holder}")
            print(f"Account Type  : {account.acc_type}")
            print(f"Current Balance: ₹{account.get_balance()}")
            print("*Transaction history logs will hook into your DB layer here.*")

    def customer_details(self):
        print("\n--- CUSTOMER DETAILS ---")
        account = self._get_account()
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Holder Name   : {account.holder}")
            print(f"Account Type  : {account.acc_type}")
            print(f"Available Fund: ₹{account.get_balance()}")

    def bank_report(self):
        print("\n--- BANK REPORT ---")
        if not self.accounts:
            print("No accounts exist in the ledger system.")
            return
        print(f"{'Acc Number':<12}{'Holder Name':<20}{'Type':<12}{'Balance':<10}")
        print("-" * 55)
        for acc_num, account in self.accounts.items():
            print(f"{acc_num:<12}{account.holder:<20}{account.acc_type:<12}₹{account.get_balance():<10}")


# --- Execution Driver ---
def main():
    bank = BankSystem()

    while True:
        print("\n========== XYZ BANK ==========")
        print("1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Balance")
        print("6. Mini Statement")
        print("7. Customer Details")
        print("8. Bank Report")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            bank.open_account()
        elif choice == "2":
            bank.deposit()
        elif choice == "3":
            bank.withdraw()
        elif choice == "4":
            bank.transfer()
        elif choice == "5":
            bank.balance_inquiry()
        elif choice == "6":
            bank.mini_statement()
        elif choice == "7":
            bank.customer_details()
        elif choice == "8":
            bank.bank_report()
        elif choice == "9":
            print("\nExiting system... Thank you for using XYZ Bank!")
            break
        else:
            print("Invalid execution choice. Please choose between 1 and 9.")

if __name__ == "__main__":
    main()