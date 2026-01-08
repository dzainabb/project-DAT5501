import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset and filter to 2024

def load_data(filepath='data/combined_data.csv'):
    combined = pd.read_csv(filepath)
#clean columns and filter year - debugging issues
    combined.columns = combined.columns.str.strip()
    combined['Year'] = pd.to_numeric(combined['Year'], errors='coerce').astype('Int64')

    combined= combined[combined['Country Code'].notna()]
    data = combined[combined['Year'] == 2023]
    data = data[
        ['Country Name',
        'Country Code',
        'Year',
        'Fertility Rate',
        'Female employment (%)',
        'GDP per capita',
        'Urban Population (%)'
        ]]
    data = data.dropna()
    return data

# train Decision Tree Regressor
data_model = load_data()

features = ['Female employment (%)',
        'GDP per capita',
        'Urban Population (%)'
]
    
x = data_model[features]
y = data_model['Fertility Rate']

#split into training and testing sets

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

#train model

tree = DecisionTreeRegressor(
    max_depth = 4,
    min_samples_leaf = 5,
    random_state =42)

tree.fit(x_train, y_train)

#predict and evaluate

y_prediction = tree.predict(x_test)

rmse = mean_squared_error(y_test,y_prediction) ** 0.5
r2 = r2_score (y_test, y_prediction)

print(f"Root Mean Squared Error: {rmse}")
print(f"R^2 Score: {r2}")

#PLOT

importances = pd.Series(
    tree.feature_importances_
    , index = features).sort_values()

plt.figure(figsize=(10,6))
importances.plot(kind='barh')
plt.xlabel("Relative Importance")
plt.title("Decision Treee Feature Importance for Fertility Rate(2024)")
plt.tight_layout()
plt.show()

