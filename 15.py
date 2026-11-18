import pandas as pd

df = pd.DataFrame({'Likes': [10, 20, 10, 30, 20, 10, 40]})

print(df['Likes'].value_counts())
