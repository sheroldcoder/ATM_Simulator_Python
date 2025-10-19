balance = 10000
pin = "1234"
print("Welcome to Python Bank ATM🏦")
entered_pin = input("Enter your PIN: ")
if entered_pin == pin:
    while True:
        print("\n===== MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = float(input("Choose an option (1-4): "))
        if choice==1:
            print(f"\nYour current balance is ₹{balance}")
        elif choice==2:
            amount = float(input("Enter amount to deposit:  ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid amount!")
        elif choice==3:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Invalid amount!")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn succesfully.")
        elif choice==4:
            print("Thank you for using Python bank ATM!👋")
            break
        else:
            print("Invalid choice! Try again.")
else:
    print("❌ Incorrect PIN Access Denied.")
