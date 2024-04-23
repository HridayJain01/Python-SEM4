import pandas as pd

# 60) Create and display DataFrame from dictionary with index labels
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]}
df = pd.DataFrame(data, index=['ID1', 'ID2', 'ID3'])
print("DataFrame from specified dictionary with index labels:")
print(df)

# 61) Display summary of basic information about DataFrame
print("\nSummary of basic information about DataFrame:")
print(df.info())

# 62) Select 'name' and 'score' columns
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'score': [80, 75, 90]}
df = pd.DataFrame(data)
print("\nSelected 'name' and 'score' columns:")
print(df[['name', 'score']])

# 63) Calculate mean of all students' scores
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'score': [80, 75, 90]}
df = pd.DataFrame(data)
mean_score = df['score'].mean()
print("\nMean of all students' scores:", mean_score)
