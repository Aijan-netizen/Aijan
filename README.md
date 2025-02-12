# SECOND ASSIGNMENT 
# Book Class 
This project contains a `Book` class written in Python. It demonstrates object-oriented programming by defining attributes and methods for a book.
# Class Description  
 - Attributes:
   - 'title' (str): The title of the book.
   - 'author' (str): The author of the book.
   - 'ISBN' (str): The International Standard Book Number of the book (optional).
   - 'price' (float): The price of the book (optional).
 - Constructors:
   - Parameterized constructor: Initializes all attributes with specific values.
   - Default constructor: Initializes attributes with default values (None for string attributes and 0.0 for price).
 - Methods:  
   - 'info()' - Displays book details(title, author, ISBN, price).  
   - 'read()' - Simulates reading the book by printing a message "You are reading (book title).". 

# THIRD ASSIGNMENT
# Personal Account Management
This is a Python program to manage a personal bank account. It allows users to:
 - Deposit money
 - Withdraw money (with balance checks)
 - Check account balance
 - View transaction history.

The program uses two classes:
 - `Amount`: Represents a single transaction (deposit or withdrawal).
 - `PersonalAccount`: Manages the account, including balance, deposits, withdrawals, and transaction history.
# How It Works
 - Account Setup:
   - The user provides their account number and name.
 - Menu Options:
   - Deposit (1): Adds money to the account.
   - Withdraw (2): Removes money from the account, with a check to ensure there are sufficient funds.
   - Check Balance (3): Displays the current balance.
   - Transaction History (4): Shows all past transactions (deposits and withdrawals).
   - Exit (5): Exits the program.
##  How It Works  
### 🔹 Account Setup:  
- The user provides their **account number** and **name**.  
### 🔹 Menu Options:  
1️⃣ **Deposit** – Adds money to the account.  
2️⃣ **Withdraw** – Removes money from the account, with a check to ensure there are sufficient funds.  
3️⃣ **Check Balance** – Displays the current balance.  
4️⃣ **Transaction History** – Shows all past transactions (deposits and withdrawals).  
5️⃣ **Exit** – Exits the program.  

---

## 🖥 Example Code Execution  

```bash
Enter account number: 240102026  
Enter account holder name: Aijan  
markdown
Copy
Edit
1. Deposit  
2. Withdraw  
3. Check Balance  
4. Transaction History  
5. Exit  
bash
Copy
Edit
Choose an option: 1  
Enter deposit amount: 200  
Deposited 200 successfully.  
bash
Copy
Edit
Choose an option: 2  
Enter withdrawal amount: 2300  
Insufficient funds  
bash
Copy
Edit
Choose an option: 3  
Current Balance: 200  
bash
Copy
Edit
Choose an option: 4  
2025-02-10 12:30:45 - DEPOSIT: 200  
bash
Copy
Edit
Choose an option: 5  
Exiting program...  
📂 Project Structure
bash
Copy
Edit
/PersonalAccountManagement
│── main.py                   # Main program file  
│── account.py                 # Contains the Amount and PersonalAccount classes  
│── test_cases/                # Folder for test cases  
│   ├── test_deposit.py  
│   ├── test_withdraw.py  
│   ├── test_balance.py  
│── UML_Diagram.png            # UML diagram of the project  
│── README.md                  # Documentation


### What I Have Done
 - Created the `Amount` class to handle transactions (deposits and withdrawals).
 - Created the `PersonalAccount` class to manage the account balance and transaction history.
 - Implemented a menu system for user interaction.
 - Added balance checks before withdrawals to prevent overdraft.
