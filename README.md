<<<<<<< HEAD
# 🏦 ATM Cash Withdrawal Simulator (Python)

A simple **Python-based ATM simulation program** that allows users to **check balance, deposit money, withdraw cash,** and **exit** securely with a PIN verification system.

---

## 🚀 Features

- **PIN Authentication:** Ensures only authorized access.  
- **Check Balance:** View current account balance.  
- **Deposit Money:** Add funds to your account.  
- **Withdraw Money:** Withdraw cash safely (with balance check).  
- **Exit Option:** Gracefully end the session.  

---

## 🧑‍💻 How It Works

The ATM starts with:

- **Initial balance:** ₹10,000  
- **Default PIN:** `1234`

Follow the on-screen menu to perform banking actions.

---

## 🧩 Code Overview

The program uses:
- `while True` loop for continuous user access until exit.
- `if-elif` structure for menu choices.
- Basic input validation for deposits and withdrawals.

---

## 💾 Setup Instructions

1. Open **VS Code**.
2. Create a new folder named `ATM_Simulator`.
3. Inside the folder, create a file called **`atm_simulator.py`**.
4. Copy and paste the following code:

```
balance = 10000
pin = "1234"

print("Welcome to Python Bank ATM 🏦")
entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\n===== MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice =float(input("Choose an option (1-4): "))

        if choice == "1":
            print(f"\nYour current balance is ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Invalid amount!")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")

        elif choice == "4":
            print("Thank you for using Python Bank ATM! 👋")
            break

        else:
            print("Invalid choice! Try again.")
else:
    print("❌ Incorrect PIN. Access Denied.")
```

5. Save the file.
6. Run the program in the terminal:
   ```
   python atm_simulator.py
   ```

## 🧠 Example Interaction

Welcome to Python Bank ATM 🏦
Enter your PIN: 1234

===== MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 1

Your current balance is ₹10000

## ⚙️ Technologies Used

- **Programming Language:** Python 3.x  
- **IDE Recommendation:** VS Code or PyCharm  

## 📜 License

This project is open for learning and educational use only. You can modify and reuse it freely.

## 🤝 Author

**Developed by:** Sherold Crasta
=======
# ATM_Simulator_Python
ATM Cash Withdrawal Simulator in Python
>>>>>>> b786b1e993cbc4be02645791fe9d8554c68f5987
