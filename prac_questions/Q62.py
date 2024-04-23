import pandas as pd

# Sample DataFrame
data = {'name': ['John', 'Anna', 'Peter', 'Linda'],
        'age': [28, 35, 40, 25],
        'score': [85, 90, 88, 92]}

df = pd.DataFrame(data)

# Select 'name' and 'score' columns using indexing operator []
selected_columns = df[['name', 'score']]

# Alternatively, you can use loc[] accessor
# selected_columns = df.loc[:, ['name', 'score']]

# Display the selected columns
print("Selected columns 'name' and 'score':")
print(selected_columns)
