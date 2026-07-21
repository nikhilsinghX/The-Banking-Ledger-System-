
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.holder = account_holder
        self._balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            return True
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")
        return False

    def check_balance(self):
        return self._balance


def main():
    print("=== WELCOME TO THE BANK ===")
    name = input("Enter your name to open an account: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Balance Inquiry")
        print("5. Customer Details")
        print("6. mini statement")
        print("7. Bank report")
        print("8. Exit")
        
        choice = input("Enter your choice (1-): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            amount = float(input("Enter amount to transfer: "))
            
        elif choice == "9":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()