# Create a simple menu-driven banking system that allows a user to perform basic banking operations on a single bank account.


# Menu Driven
def display_menu():
    print(f"""
===== BANKING SYSTEM =====

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
""")

# 1. Check Balance
def check_balance(balance):
    return f"Current Balance: ₹{balance}"

# 2. Deposit Money
def deposit_money(balance,deposit_amount):

    if not isinstance(deposit_amount,int):
        raise TypeError("Deposit amount must be an integer.")

    if deposit_amount <= 0:
        raise ValueError("deposit amount must be greater than 0")

    balance += deposit_amount

    return balance

# 3. Withdraw Money
def withdraw_money(balance,withdraw_amount):

    if not isinstance(withdraw_amount,int):
        raise TypeError("withdraw amount must be greater than 0")

    if withdraw_amount <= 0:
        raise ValueError("withdraw amount must be greater than 0")

    if withdraw_amount > balance:
        raise ValueError("Insufficient balance")

    balance -= withdraw_amount

    return balance

# 4. Exit

def exit():
    return "Thank you for using the Banking System."


def main():
    # Initial Account details
    Account_Holder = "Rohan Bangar"
    balance = 10000 

    while True:

        # Display menu for customer's
        display_menu()

        try:
            choice = int(input("Enter Your choice: "))
        except ValueError:
            print("Choice must be an integer")
            continue

        if choice == 1:
            print(check_balance(balance))

        elif choice == 2:
            try:
                deposit_amount = int(input("Enter deposit amount: "))
                balance = deposit_money(balance,deposit_amount)
            except ValueError as error:
                print(error)
                continue

            print(f"""
₹{deposit_amount} deposite successfully
current balance: ₹{balance}
            """)

        elif choice == 3:
            try:
                withdraw_amount = int(input("Enter withdraw amount: "))
                balance = withdraw_money(balance,withdraw_amount)
            except ValueError as error:
                print(error)
                continue

            print(f"""
₹{withdraw_amount} withdraw successfully
current balance: ₹{balance}
            """)

        elif choice == 4:
            print(exit())

        else:
            print("Invalid choice. Please enter between 1-4")

# Calling Main function

if __name__ == "__main__":
        main()
