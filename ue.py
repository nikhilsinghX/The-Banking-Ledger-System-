# # Heart outline pattern in Python
# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col % 3 != 0) or \
#            (row == 1 and col % 3 == 0) or \
#            (row - col == 2) or \
#            (row + col == 8):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
# #     print()
# se=input("Enter the sentence : ")
# str=se.split()
# print("The words in the sentence are : ", str)
# str.reverse()
# print("The words in the reverse order are : ", str)
# print("The words in the reverse order are : ", " ".join(str))
# s="aabbbcdddeeff"
# for i in s:
#     if s.count(i)==1:
#         print(i )
#         break
print("============== XYZ BANK =================")
while True:
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        balance = 0
        print(f"Account created for {name} with account number {account_number}. Initial balance is {balance}.")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited {amount}. New balance is {balance}.")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew {amount}. New balance is {balance}.")
        else:
            print("Insufficient funds.")
    elif choice == '4':
        print(f"Current balance is {balance}.")
    elif choice == '5':
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please try again.")
