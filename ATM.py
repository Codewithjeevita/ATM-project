balance = 1000  # Initial balance

def check_balance():
    print(f"\n Your current balance is: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f" ₹{amount} deposited successfully!")
    else:
        print(" Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance!")
    elif amount <= 0:
        print(" Invalid amount!")
    else:
        balance -= amount
        print(f" ₹{amount} withdrawn successfully!")

def atm_menu():
    print("\n Welcome to Python ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

while True:
    atm_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print(" Thank you for using Python ATM. Goodbye!")
        break
    else:
        print(" Invalid choice! Please select 1 to 4.")