import pandas as pd
import matplotlib.pyplot as plt

# Function to load CSV files
def load_data():
    
    fertility= pd.read_csv('/Users/sabiqadar/Desktop/project-DAT5501/data/children-per-woman-un.csv')

    fertility['Year'] = fertility['Year'].astype(int)

    return fertility

countries = {
    'United Kingdom': 'GBR',
    'India': 'IND',
    'China': 'CHN',
    'Brazil': 'BRA',
    'Germany': 'DEU'
}
fertility_df= load_data()

fertility_df = fertility_df[fertility_df['Code'].isin(countries.values())]
fertility_df['country'] = fertility_df["Entity"]

fertility_df=fertility_df[(fertility_df['Year'] >=1960) & (fertility_df['Year'] <=2023)]

#PLOT
plt.figure(figsize=(10, 6))
for country in fertility_df['country'].unique():
    subset =fertility_df[fertility_df['country'] == country]
    plt.plot(
        subset['Year'],
        subset['Fertility rate - Sex: all - Age: all - Variant: estimates'],
        label=country
    )

plt.xlabel('Year')
plt.ylabel('Total Fertility Rate')
plt.title('Total Fertility Rate Over Time (1960-2023)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
