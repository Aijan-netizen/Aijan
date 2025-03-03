import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],  # Column A has one missing value
    'B': [np.nan, 2, 3, 4, 5],  # Column B has one missing value
    'C': ['a', 'b', 'b', np.nan, 'a']  # Column C has one missing value })

# Checking the number of missing values in each column
print("Missing values:\n", df.isnull().sum())

# Filling missing numerical values:
# - Column A: Replace NaN with the mean value
df['A'].fillna(df['A'].mean(), inplace=True)
# - Column B: Replace NaN with the median value  
df['B'].fillna(df['B'].median(), inplace=True)

# Filling missing categorical values with the mode (most frequent value)
df['C'].fillna(df['C'].mode()[0], inplace=True)

# Display the updated DataFrame
print("\nDataFrame after handling missing values:\n", df)
