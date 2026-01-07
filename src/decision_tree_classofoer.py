import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text
import pydotplus
from matplotlib import pyplot as plt
from io import StringIO
from PIL import Image

#load data
df = pd.read_csv("data/combined_data.csv")

# Clean column 
df.columns = df.columns.str.strip()

df = df[df["Year"] == 2023].dropna()

# Create a classification target:
# 1 = High fertility, 0 = Low fertility
df["Fertility_Class"] = (df["Fertility Rate"] > df["Fertility Rate"].median()).astype(int)

# Features
features = [
    "Female employment (%)",
    "GDP per capita",
    "Urban Population (%)"
]

X = df[features]
y = df["Fertility_Class"]

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model - decision tree classifier
clf = tree.DecisionTreeClassifier(
    max_depth=4,
    min_samples_leaf=5,
    random_state=42
)

clf.fit(X_train, y_train)

# evaluare and predict
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {acc:.3f}\n")


# making a visual plot of the tree using graphviz
dot_data = StringIO()
tree.export_graphviz(
    clf,
    out_file=dot_data,
    feature_names=features,
    class_names=["Low", "High"],
    filled=True,
    rounded=True,
    special_characters=True
)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("decision_tree.png")

# display the PNG - and save as file
img = Image.open("decision_tree.png")
plt.figure(figsize=(12, 12))
plt.imshow(img)
plt.axis("off")
plt.show()

#feature importance plot
importances = pd.Series(clf.feature_importances_, index=features).sort_values()

plt.figure(figsize=(8, 5))
importances.plot(kind="barh")
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()
