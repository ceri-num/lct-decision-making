from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt
import random

# Get iris:
iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Sample:
size= len(X)
for x in range(10) :
    i = random.randint(0, size)
    print(f"{X[i]} -> {y[i]}")

print("...")

# Tree:
plt.figure()
tree.plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()

# Prediction:
sample= [6.7, 2.0, 0.9, 0.1]
print(f"{sample} -> {clf.predict([[1, 1, 1, 1]])}")
