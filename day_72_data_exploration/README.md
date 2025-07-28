# Day 72 - Data Analysis with Pandas

Welcome to Day 72 of the 100 Days of Code Python Bootcamp! Today we dive deep into data analysis using pandas, one of the most powerful libraries for data manipulation and analysis in Python.

## 🎯 Learning Objectives

This lesson covers essential pandas DataFrame operations that every data analyst should master. You'll learn how to explore, clean, and manipulate data effectively using pandas methods.

## 📚 Key Learning Points

### 1. DataFrame Exploration
Learn how to get familiar with your dataset using basic exploration methods:

- **`.head()`** - View the first few rows of your DataFrame
- **`.tail()`** - View the last few rows of your DataFrame  
- **`.shape`** - Get the dimensions (rows, columns) of your DataFrame
- **`.columns`** - Access the column names of your DataFrame

```python
# Example usage
df.head()        # Shows first 5 rows by default
df.tail(10)      # Shows last 10 rows
df.shape         # Returns (rows, columns) tuple
df.columns       # Returns column names
```

### 2. Data Cleaning
Handle missing data and clean your DataFrame:

- **`.isna()` / `.findna()`** - Identify NaN (Not a Number) values
- **`.dropna()`** - Remove rows or columns with missing values

```python
# Check for missing values
df.isna().sum()  # Count NaN values per column

# Remove rows with missing values
df_clean = df.dropna()
```

### 3. Data Access and Selection
Master different ways to access data in your DataFrame:

- **Single column**: `df['column_name']`
- **Multiple columns**: `df[['col1', 'col2', 'col3']]`
- **Individual cells**: `df['column_name'][index]` or `df['column_name'].loc[index]`

```python
# Accessing data examples
names = df['Name']                    # Single column
subset = df[['Name', 'Age', 'City']]  # Multiple columns
first_name = df['Name'][0]            # Individual cell
specific_value = df['Name'].loc[5]    # Using .loc
```

### 4. Finding Extremes
Locate maximum and minimum values and their positions:

- **`.max()`** - Find the largest values
- **`.min()`** - Find the smallest values
- **`.idxmax()`** - Find the index of maximum values
- **`.idxmin()`** - Find the index of minimum values

```python
# Finding extremes
highest_value = df['Sales'].max()      # Maximum value
lowest_value = df['Sales'].min()       # Minimum value
max_index = df['Sales'].idxmax()       # Index of maximum
min_index = df['Sales'].idxmin()       # Index of minimum
```

### 5. Data Manipulation
Sort your data and add new information:

- **`.sort_values()`** - Sort DataFrame by column values
- **`.insert()`** - Add new columns to your DataFrame

```python
# Sorting and inserting
df_sorted = df.sort_values('Age')                    # Sort by Age
df_sorted = df.sort_values('Age', ascending=False)   # Descending order

# Insert new column
df.insert(1, 'Full_Name', df['First'] + ' ' + df['Last'])
```

### 6. Grouping and Aggregation
Create Excel-style pivot tables using groupby operations:

- **`.groupby()`** - Group data by categories for analysis

```python
# Grouping examples
grouped = df.groupby('Category').sum()     # Sum by category
avg_by_dept = df.groupby('Department')['Salary'].mean()  # Average salary by department
```

## 🛠️ Project Structure

```
day_72_data_exploration/
├── main.py          # Main analysis script
├── data/            # Data files directory
├── README.md        # This file
└── .ipynb_checkpoints/  # Jupyter notebook checkpoints
```

## 🚀 Getting Started

1. Ensure you have pandas installed:
   ```bash
   pip install pandas
   ```

2. Run the main analysis script:
   ```bash
   python main.py
   ```

3. Explore the data files in the `data/` directory

## 📈 Skills Developed

By the end of this lesson, you will be able to:

- ✅ Explore and understand the structure of any DataFrame
- ✅ Identify and handle missing data appropriately  
- ✅ Access specific data points and subsets efficiently
- ✅ Find statistical extremes in your datasets
- ✅ Sort and organize data meaningfully
- ✅ Create grouped analyses and pivot table-style summaries
- ✅ Add calculated columns to enhance your datasets

## 🔗 Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [DataFrame API Reference](https://pandas.pydata.org/docs/reference/frame.html)
- [Data Cleaning Guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)

## 🎉 Next Steps

These fundamental pandas operations form the foundation of data analysis. Practice these methods with different datasets to become proficient in data exploration and manipulation!

---

*Day 72 of 100 Days of Code - Python Pro Bootcamp*
