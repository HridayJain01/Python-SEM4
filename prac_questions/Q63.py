import pandas as pd

# Sample DataFrame
data = {'name': ['John', 'Anna', 'Peter', 'Linda'],
        'score': [85, 90, 88, 92]}

df = pd.DataFrame(data)

# Calculate the mean of all students' scores
mean_score = df['score'].mean()

# Display the mean score
print("Mean of all students' scores:", mean_score)
