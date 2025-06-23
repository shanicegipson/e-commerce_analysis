import pandas as pd

data = { 'name': ['Shanice', 'Honesty', 'Lexi', 'LaTrease'],
    'age': [32, 6, 31, 30],
    'gender': ['female', 'female', 'female', 'female']
}

df = pd.DataFrame(data)

print(df)

print('Mean age:', df['age'].mean())