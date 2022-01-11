from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Iris

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset.data,iris_dataset.target,random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)

X_new = np.array([
    [5,2.9,1,0.2]
])
prediction = knn.predict(X_new)

print("Prediction : ",format(prediction))
print('Prediction target name : ',format(iris_dataset.target_names[prediction]))

# Use test data set
y_pred = knn.predict(X_test)
print('Prediction on test set : ',format(y_pred))
# Score test
score = np.mean(y_pred == y_test)
print('Score : ',score * 100)