import pandas as pd

# Sample dictionary with index labels
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 40, 25],
        'City': ['New York', 'Paris', 'London', 'Sydney']}

# Specified index labels
index_labels = ['A', 'B', 'C', 'D']

# Create DataFrame with index labels
df = pd.DataFrame(data, index=index_labels)

# Display the DataFrame
print("DataFrame with specified index labels:")
print(df)
