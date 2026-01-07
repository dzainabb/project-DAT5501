import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/fertility_rate.csv')

uk_data = data[data['Code'] == 'GBR']
uk_data = uk_data.sort_values(by='Year')

years = uk_data['Year'].values
uk = uk_data['Fertility rate - Sex: all - Age: all - Variant: estimates'].values

# Split the data into training and testing sets
test_years = 10

x_train = years[:-test_years]
y_train = uk[:-test_years]

x_test = years[-test_years:]
y_test = uk[-test_years:]

orders = range(1,10)
bic_values = []

#plot all data
plt.figure(figsize=(10, 6))
plt.plot(years, uk, 'k-',linewidth=2, label= 'observed')

# BIC calculation and polynomial fitting - plots different orders to see which fits best
for deg in orders:
    coefficients = np.polyfit(x_train, y_train, deg)
    model = np.poly1d(coefficients)

    y_predicted = model(x_test)

    residuals = y_test - y_predicted
    rss = np.sum(residuals**2)
    n = len(y_test)
    k = deg +1

    bic = n *np.log(rss/n) + k* np.log(n)
    bic_values.append(bic)


    plt.plot(x_test,
              y_predicted,
              '--', 
             linewidth =1.5,
             label=f'Degree {deg}')
    
plt.xlabel('Year')
plt.ylabel('Total Fertility Rate')
plt.title('Polynomial Fits to UK Fertility Data with BIC')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#BIC vs polynomical order

plt.figure(figsize=(8, 5))
plt.plot(orders, bic_values, 'o-', linewidth=2)
plt.xlabel('Polynomial Order')
plt.ylabel('BIC - Bayesian Information Criterion')
plt.title('Model Selection: UK Fertility Data with BIC')
plt.grid(True)
plt.tight_layout()
plt.show()
