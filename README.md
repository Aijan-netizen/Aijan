# EIGHTH ASSIGNMENT 
# Employee Management System (SQLite + Python)

This is a simple command-line application written in Python that manages employee records using SQLite.

## Features

- Add a new employee  
- View all employees  
- Get employee by ID  
- Update employee information  
- Delete employee by ID  

## File Structure

- `employee.py` – Employee data model  
- `employee_dao.py` – Data access layer (database operations)  
- `main.py` – Main script to run the program  
- `employee_db.db` – SQLite database (created automatically)

## Technologies Used

- Python 3  
- SQLite (local database)  

##Example output
```
All Employees:
ID: 1, Name: Aizhan, Position: Teacher, Salary: 100000.0, Hire Date: 2025-04-11

Employee with ID = 1:
ID: 1, Name: Aizhan, Position: Teacher, Salary: 100000.0, Hire Date: 2025-04-11

After Deletion:
(no employees found)
```
