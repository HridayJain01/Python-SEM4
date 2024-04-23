import pandas as pd

# Sample dictionary
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 40, 25],
        'City': ['New York', 'Paris', 'London', 'Sydney']}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)
