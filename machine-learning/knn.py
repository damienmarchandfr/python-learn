from sklearn.model_selection import train_test_split
from mglearn.datasets import make_forge
from sklearn.neighbors import KNeighborsClassifier

X, y = make_forge()

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

clf = KNeighborsClassifier(3)

clf.fit(X_train,y_train)

prediction = clf.predict(X_test)

score = clf.score(X_test,y_test)

print(score)
