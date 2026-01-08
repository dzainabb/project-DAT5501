#data cleaning 

import pandas as pd

#load data
def load_data():
    fertility = pd.read_csv('data/fertility_rate.csv')
    employment = pd.read_csv('data/female_employment.csv')

# Rename columns for consistency
    fertility = fertility.rename(columns={ "Entity": "Country Name", 
                                          "Code": "Country Code",
                                          "Fertility rate - Sex: all - Age: all - Variant: estimates": "Fertility Rate" })
    
    employment = employment.rename(columns={ "Entity": "Country Name",
                                          'Code': "Country Code",
                                          "Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)": "Female employment (%)" })
    
    return fertility[["Country Name", "Country Code", "Year", "Fertility Rate"]],\
          employment[["Country Name", "Country Code", "Year", "Female employment (%)"]]

# Convert wide format to long format
def wide_to_long():
        gdp = pd.read_csv('data/GDP_per_capita.csv', skiprows=4, sep =',', engine='python')
        urban = pd.read_csv('data/urban_population.csv', skiprows=4, sep =',', engine='python')

        gdp_long = gdp.melt(
        id_vars= [ 'Country Name', "Country Code"],
        var_name='Year',
        value_name= 'GDP per capita '
        )
        gdp_long['Year'] = pd.to_numeric(gdp_long['Year'], errors='coerce').astype('Int64')
        
        urban_long = urban.melt(
        id_vars= [ 'Country Name', "Country Code"],
        var_name='Year',
        value_name= 'Urban Population (%)'
        )
        urban_long['Year'] = pd.to_numeric(urban_long['Year'], errors='coerce').astype('Int64')
        
        return gdp_long[["Country Name", "Country Code", "Year", "GDP per capita "]],\
              urban_long[["Country Name", "Country Code", "Year", "Urban Population (%)"]]

# Combine datasets
def combine():
    fertility, employment = load_data()
    gdp_long, urban_long = wide_to_long()

    combined = pd.merge(fertility, employment, on=['Country Name', 'Country Code', 'Year'], how='outer')
    combined = pd.merge(combined, gdp_long, on=['Country Name', 'Country Code', 'Year'], how='outer')
    combined = pd.merge(combined, urban_long, on=['Country Name', 'Country Code', 'Year'], how='outer')



    combined = combined.dropna(subset=[ 'Year'])
    return combined

if __name__ == "__main__":
    combined = combine()
    combined.to_csv('data/combined_data.csv', index=False)


