import pandas as pd

df = pd.read_csv('data/female_employment.csv')

print(df['Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)'].describe())
print(df.head())