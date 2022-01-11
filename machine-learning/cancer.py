from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=66)

# test KNN
knn_settings = range(1,11)

for knn_s in knn_settings:
    clf = KNeighborsClassifier(knn_s)
    clf.fit(X_train,y_train)
    score_training = clf.score(X_train,y_train)
    score_accuracy = clf.score(X_test,y_test)
    print(knn_s,score_training,score_accuracy)


