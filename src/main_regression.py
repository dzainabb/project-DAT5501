import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset + merge
employemnt = pd.read_csv('data/female_employment.csv')
fertility = pd.read_csv('`data/fertility_rate.csv')

#only having 2023 data
employemnt = employemnt[employemnt['Year'] == 2023]
fertility = fertility[fertility['Year'] == 2023]


df = pd.merge(employemnt, fertility, on=['Entity', 'Year', 'Code'])
# Highlight countries to annotate
highlight = ['China', 'India', 'Somalia','Yemen',  'Nigeria', 'Mexico', 'Chad', 'United Kingdom', 'South Korea']
# Prepare data for regression
x = df[['Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)']]
y = df['Fertility rate - Sex: all - Age: all - Variant: estimates']

# Create and fit the model

model = LinearRegression()
model.fit(x, y)

# Print the coefficients on grpaph

stats_print= { 'Intercept': model.intercept_,
              'Slope': model.coef_[0],
              'R^2': model.score(x, y)
             }

plt.text(0.05, 0.95, f"Intercept: {stats_print['Intercept']:.2f}\nSlope: {stats_print['Slope']:.2f}\nR^2: {stats_print['R^2']:.2f}",
            transform=plt.gca().transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))


#PLOT
y_pred = model.predict(x)
plt.scatter(x,y,color='blue', label='All countries data')

# Highlight specific countries
highlight_data = df[df['Entity'].isin(highlight)]

plt.scatter(
    highlight_data['Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)'],
    highlight_data['Fertility rate - Sex: all - Age: all - Variant: estimates'],
    color='green',
    label='Highlighted Countries'
)
# Annotate highlighted countries
for _, row in highlight_data.iterrows():
    plt.text(
        row['Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)'],
        row['Fertility rate - Sex: all - Age: all - Variant: estimates'],
        row['Entity'],
        fontsize=20,
        color='red'
    )
# Plot regression line
plt.plot(x,y_pred, color='red', label='Regression Line')
plt.xlabel('Female labour force participation rate (%)')
plt.ylabel('Fertililty Rate')
plt.title('Female Labour Force Participation Rate vs Fertility Rate')
plt.legend()
plt.show()

