import pandas as pd
import matplotlib.pyplot as plt

# Function to load CSV files
def load_data(filepath='data/fertility_rate.csv'):
    
    fertility= pd.read_csv(filepath)

    fertility['Year'] = fertility['Year'].astype(int)

    return fertility
# Filter data for specific countries and years
countries = {
    'United Kingdom': 'GBR',
    'India': 'IND',
    'China': 'CHN',
    'United States': 'USA',
    'France': 'FRA',
    'South Korea': 'KOR'
}
fertility_df= load_data()

fertility_df = fertility_df[fertility_df['Code'].isin(countries.values())]
fertility_df['country'] = fertility_df["Entity"]
# Filter years between 1960 and 2023
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
# custom plot
plt.xlabel('Year')
plt.ylabel('Total Fertility Rate')
plt.title('Total Fertility Rate Over Time (1960-2023)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
