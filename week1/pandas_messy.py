
### Classroom Activity 

## Refactoring Messy Data with Pandas

import pandas as pd


def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_mean(df, column):
    """Calculate the average of a column."""
    return df[column].mean()


def calculate_max(df, column):
    """Find the maximum value in a column."""
    return df[column].max()


def filter_by_value(df, column, value):
    """Filter rows based on a specific column value."""
    return df[df[column] == value]


# Load dataset
df = load_csv("iris.csv")

# Calculate statistics
avg = calculate_mean(df, "sepal_length")
mx = calculate_max(df, "petal_width")

# Filter setosa rows
setosa = filter_by_value(df, "species", "setosa")

# Display results
print("Average sepal length:", avg)
print("Max petal width:", mx)
print("\nFirst five setosa rows:")
print(setosa.head())

