#first Q
import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],  # Missing value in column A
    'B': [np.nan, 2, 3, 4, 5],  # Missing value in column B
    'C': ['a', 'b', 'b', np.nan, 'a']  # Missing value in column C
})
# Checking for missing values
print("Missing values:\n", df.isnull().sum())

# Filling numeric NaN values
df['A'].fillna(df['A'].mean(), inplace=True)  # Replace NaN with mean value
df['B'].fillna(df['B'].median(), inplace=True)  # Replace NaN with mean value

# Filling categorical NaN values
df['C'].fillna(df['C'].mode()[0], inplace=True)  # Replace with most frequent value (mode)
print("\nDataFrame after filling missing values:\n", df)


#second Q
import pandas as pd

# Creating a DataFrame with categorical data
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Green'],
    'Size': ['S', 'M', 'L', 'M', 'S'] })

# Label encoding (convert categories to numbers)
df['Color_Label'] = df['Color'].astype('category').cat.codes

# One-hot encoding (create binary columns for each category)
df_one_hot = pd.get_dummies(df, columns=['Size'])
print("Label Encoding:\n", df[['Color', 'Color_Label']])
print("\nOne-Hot Encoding:\n", df_one_hot)


#third Q
import pandas as pd

# Creating a DataFrame with duplicate rows
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 4, 4],  # Repeating values in column A
    'B': ['x', 'y', 'y', 'z', 'z', 'z'] })

# Identifying duplicate rows (True = duplicate)
print("Duplicate Rows:\n", df.duplicated())

# Removing duplicates (keeps the first occurrence)
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:\n", df_no_duplicates)


# forth Q
import pandas as pd
import numpy as np

# Creating a DataFrame with numerical data
df = pd.DataFrame({'Value': [10, 20, 30, 40, 50]})

# Min-Max Scaling: Scales values between 0 and 1 using the formula (X - X_min) / (X_max - X_min).
df['MinMax_Scaled'] = (df['Value'] - df['Value'].min()) / (df['Value'].max() - df['Value'].min())

# Z-score Normalization: Normalizes values to have a mean of 0 and a standard deviation of 1 using (X - mean) / std.
df['Z_Score_Scaled'] = (df['Value'] - df['Value'].mean()) / df['Value'].std()
print(df)


# fifth Q
import pandas as pd
import numpy as np

# Creating a dataset with an outlier
df = pd.DataFrame({'Values': [10, 12, 11, 13, 100]})  # 100 is an outlier

# Detecting outliers using the IQR method
Q1 = df['Values'].quantile(0.25)  # 25th percentile
Q3 = df['Values'].quantile(0.75)  # 75th percentile
IQR = Q3 - Q1  # Interquartile range

# Defining lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identifying outliers
outliers = df[(df['Values'] < lower_bound) | (df['Values'] > upper_bound)]
print("Outliers:\n", outliers)

# Removing outliers
df_no_outliers = df[(df['Values'] >= lower_bound) & (df['Values'] <= upper_bound)]
print("\nDataFrame after removing outliers:\n", df_no_outliers)


