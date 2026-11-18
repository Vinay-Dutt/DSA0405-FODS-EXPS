import pandas as pd

df = pd.DataFrame({'Age': [20, 25, 20, 30, 25, 20, 35]})

print(df['Age'].value_counts())
