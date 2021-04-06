import pandas as pd

pd.set_option('display.max_colwidth', 90)

filename = 'Bugs.csv'
df = pd.read_csv(filename)
a = df['Summary']
print(a)
