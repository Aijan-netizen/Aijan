# SIXTH ASSIGNMENT 
## Personal Account Management
This is a Python program to manage a personal bank account. It allows users to:
 - Deposit money
 - Withdraw money (with balance checks)
 - Check account balance
 - View transaction history.

The program uses two classes:
 - `Amount`: Represents a single transaction (deposit or withdrawal).
 - `PersonalAccount`: Manages the account, including balance, deposits, withdrawals, and transaction history.

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
Enter account number: `240102026`  
Enter account holder name: `Aijan`  

1. Deposit  
2. Withdraw  
3. Check Balance  
4. Transaction History  
5. Exit  

Choose an option: `1`  
Enter deposit amount: `200`  
`Deposited 200 successfully`  

Choose an option: `2`  
Enter withdrawal amount: `2300`  
`Insufficient funds`

Choose an option: `3`  
Current Balance: `200`  

Choose an option: `4`  
`2025-02-10 12:30:45 - DEPOSIT: 200`  

Choose an option: `5`  
`Exiting program...`

```
---
## What I Have Done
 - Created the `Amount` class to handle transactions (deposits and withdrawals).
 - Created the `PersonalAccount` class to manage the account balance and transaction history.
 - Implemented a menu system for user interaction.
 - Added balance checks before withdrawals to prevent overdraft.
