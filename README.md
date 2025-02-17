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

#### 🔍 Expected Output:
```
Family members tuple: ('Father', 'Mother', 'Brother', 'Sister')
Type of the tuple: <class 'tuple'>
First member: Father
Last member: Sister

Attempting to append an item...
AttributeError: 'tuple' object has no attribute 'append'

Attempting to pop an item...
AttributeError: 'tuple' object has no attribute 'pop'
```

---

### 💻 2. `laptop.py`

#### ✨ Functionality:
- ✔ Defines a dictionary containing laptop details.
- ✔ Retrieves and prints the brand value.
- ✔ Adds a new key-value pair (`home: True`).
- ✔ Modifies an existing value (`year` changed to 2019).

#### 🔍 Expected Output:
```
Laptop brand: Dell

Updated dictionary:
{'brand': 'Dell', 'model': 'XPS 13', 'year': 2018, 'home': True}

Modified dictionary:
{'brand': 'Dell', 'model': 'XPS 13', 'year': 2019, 'home': True}
```

---

### 👤 3. `user.py (BTS questions part)`

#### ✨ Functionality:
- ✔ Collects user information via input prompts.
- ✔ Stores the collected data in a dictionary.
- ✔ Displays the stored information in a structured format.

#### 🔍 Expected Output:
```
Enter your name: John Doe
Enter your age: 25
Enter your favorite color: Blue

User Information:
Name: John Doe
Age: 25
Favorite Color: Blue
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
### 💊 4. Additional Pandas Implementation

#### ✨ Functionality:
- ✔ Creates and prints a Pandas `Series` for months.
- ✔ Defines a `Series` with student counts per department.
- ✔ Constructs a `DataFrame` containing exam data and prints it.
- ✔ Filters and prints rows where attempts exceed 2.

