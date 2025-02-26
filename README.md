# 4TH ASSIGNMENT
## Personal Account Management
This Python program provides a simple personal bank account management system, allowing users to:

- Deposit money
- Withdraw money (with balance checks)
- Check account balance
- View transaction history

### Features

- **Class-based Structure**: Uses `Transaction` and `BankAccount` classes for better data organization.
- **Transaction History**: Records deposits and withdrawals.
- **Balance Validation**: Prevents overdraft by checking available balance before withdrawals.
- **User-Friendly Menu**: Allows easy navigation between actions.

## How It Works

### 🔹 Account Setup:
- The user provides an **account number** and **name**.

### 🔹 Menu Options:
1️⃣ **Deposit** – Adds money to the account.  
2️⃣ **Withdraw** – Removes money from the account (if sufficient funds exist).  
3️⃣ **Check Balance** – Displays the current balance.  
4️⃣ **Transaction History** – Shows all past transactions.  
5️⃣ **Exit** – Exits the program.  

---

## 🖥 Example Execution

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
`Deposit: 200, Balance after: 200`

Choose an option: `5`  
`Exiting program...`
```

---

## Implementation Details

- **`Transaction` Class**: Represents an individual transaction.
- **`BankAccount` Class**: Manages balance and transaction history.
- **Interactive Menu**: Allows users to interact with the account easily.

## What I Have Done
- Refactored code for clarity and maintainability.
- Improved transaction recording and output format.
- Enhanced error handling and user prompts.
