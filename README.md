# First assignment README

## 📚 Overview
This project includes three Python programs that demonstrate working with tuples, dictionaries, and Pandas data structures. Each program executes specific tasks and outputs corresponding results.

---

## 📂 Programs and Expected Output

### 🏠 1. `myfamily.py`

#### ✨ Functionality:
 - ✔ Defines a tuple containing family member roles.
 - ✔ Prints the tuple and its type.
 - ✔ Accesses and prints specific items using index numbers.
 - ✔ Attempts to modify the tuple using `append()` and `pop()`, resulting in errors since tuples are immutable.

#### 🔍 Output:
```
('mother', 'father', 'sister', 'brother', 'sister')
Type of myfamily: <class 'tuple'>
First occurrence of 'sister': sister
Second occurrence of 'sister': sister
Error: 'tuple' object has no attribute 'append'
Error: 'tuple' object has no attribute 'pop'


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

---

### 💻 2. `laptop.py`

#### ✨ Functionality:
- ✔ Defines a dictionary containing laptop details.
- ✔ Retrieves and prints the brand value.
- ✔ Adds a new key-value pair (`home: True`).
- ✔ Modifies an existing value (`year` changed to 2019).

#### 🔍 Output:
```
Brand: dell
Updated laptop dictionary: {'brand': 'dell', 'model': 'alienware', 'year': 2010, 'home': True}
Modified laptop dictionary: {'brand': 'dell', 'model': 'alienware', 'year': 2019, 'home': True}


** Process exited - Return Code: 0 **
Press Enter to exit terminal
```

---

### 👤 3. `user.py (BTS questions part)`

#### ✨ Functionality:
- ✔ Collects user information via input prompts.
- ✔ Stores the collected data in a dictionary.
- ✔ Displays the stored information in a structured format.

#### 🔍 Output:
```
What is the user's name? 
BTS
What is the user's age? 
20
What is the user's country of birth? 
Korea
What is the user known for? 
You don't knoe BTS?

User Information:
Name: BTS
Age: 20
Country of Birth: Korea
Known for: You don't knoe BTS?

=== Code Execution Successful ===
```
---


# Second assignment README: Pandas Series and DataFrame

### 1. Data Types for Pandas Series
A Pandas Series can be created using the following data types:
- Lists
- Tuples
- Dictionaries
- NumPy Arrays
- Scalar values (single value repeated for index)

---

### 2. Creating a Series with Month Numbers
A Pandas Series is created where month names are used as index labels, and their respective numerical values are used as data.

**Output:**
```
Series with months:
January      1
February     2
March        3
April        4
May          5
June         6
July         7
August       8
September    9
October     10
November    11
December    12
dtype: int64
```

---

### 3. Creating a Series for Student Groups
A Pandas Series is created using a dictionary that stores the number of students in different fresh batch groups.

**Output:**
```
Series with the number of students:
MATMIE     30
MATDAIS    25
COMSE      40
COMCEH     35
dtype: int64
```

---

### 4. Creating and Displaying a DataFrame
A DataFrame is created from a dictionary containing student examination data. The dictionary includes student names, scores, number of attempts, and qualification status. The DataFrame is displayed in a structured format.

**Output:**
```
DataFrame with exam data:
        name  score  attempts qualify
a  Anastasia   12.5        1     yes
b      Dima    9.0        3      no
c  Katherine   16.5        2     yes
d     James    NaN        3      no
e     Emily    9.0        2      no
f  Michael   20.0        3     yes
g  Matthew   14.5        1     yes
h     Laura    NaN        1      no
i     Kevin    8.0        2      no
j     Jonas   19.0        1     yes
```

---

### 5. Selecting Rows Where Attempts > 2
A DataFrame filter is applied to select rows where students have attempted the examination more than 2 times.

**Output:**
```
Rows with attempts greater than 2:
      name  score  attempts qualify
b     Dima    9.0         3      no
d    James    NaN         3      no
f  Michael   20.0         3     yes
```
###  4. Additional Pandas Implementation

#### ✨ Functionality:
- ✔ Creates and prints a Pandas `Series` for months.
- ✔ Defines a `Series` with student counts per department.
- ✔ Constructs a `DataFrame` containing exam data and prints it.
- ✔ Filters and prints rows where attempts exceed 2.

