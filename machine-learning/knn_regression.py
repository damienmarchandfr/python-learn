from mglearn.datasets import make_wave
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

X, y = make_wave()

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

reg = KNeighborsRegressor(5)
reg.fit(X_train,y_train)

prediction = reg.predict(X_test)
print(prediction)

score = reg.score(X_test,y_test)

print(score)