import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 40, 25],
        'City': ['New York', 'Paris', 'London', 'Sydney']}

df = pd.DataFrame(data)

# Display summary information about the DataFrame
print("Summary of basic information about the DataFrame:")
df.info()
