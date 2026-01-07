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
chi2_dof = []

#plot all data
plt.figure(figsize=(10, 6))
plt.plot(years, uk, 'k-',linewidth=2, label= 'observed')
# CHi-squared calculation and polynomial fitting - plots different orders to see which fits best
for deg in orders:
    coefficients = np.polyfit(x_train, y_train, deg)
    model = np.poly1d(coefficients)

    y_predicted = model(x_test)

    residuals = y_test - y_predicted
    chi2 = np.sum(residuals**2)
    dof = len(y_test) - (deg + 1)

    chi2_dof.append(chi2/dof) #chi-squared per degree of freedom

    plt.plot(x_test,
              y_predicted,
              '--', 
             linewidth =1.5,
             label=f'Degree {deg}')

plt.xlabel('Year')
plt.ylabel('Total Fertility Rate')
plt.title('Polynomial Fits to UK Fertility Data with Chi-Squared per Degree of Freedom')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#chi-squared per degreee of freedom vs polynomical order

plt.figure(figsize=(8, 5))
plt.plot(orders, chi2_dof, 'o-', linewidth=2)
plt.xlabel('Polynomial Order')
plt.ylabel('Chi-Squared per Degree of Freedom')
plt.title('Model Selection :UK Fertility Data with Chi-Squared per Degree of Freedom')
plt.grid(True)
plt.tight_layout()
plt.show()

