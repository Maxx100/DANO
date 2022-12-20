from sklearn import datasets, svm
from time import sleep
from sklearn.neural_network import MLPClassifier, MLPRegressor
from random import randint
import joblib


def ceil(a):
    if a >= 0:
        return int(a + 0.5)
    return int(a - 0.5)


class MlpNet:  # Regressor/Classifier
    def __init__(self):
        self.mlp = MLPRegressor(hidden_layer_sizes=(5, 5), alpha=1, max_iter=500, power_t=0.5, tol=0.0001)

    def predict(self, database):
        return self.mlp.predict(database)

    def save(self):
        joblib.dump(self.mlp, "mlp.pkl")

    def load(self):
        self.mlp = joblib.load("mlp.pkl")

    def fit(self, database, target):
        self.mlp.fit(database, target)


class ClfNet:  # vectors
    def __init__(self):
        self.clf = svm.SVC(gamma=0.001, C=100.)

    def predict(self, database):
        return self.clf.predict(database)

    def save(self):
        joblib.dump(self.clf, "clf.pkl")

    def load(self):
        self.clf = joblib.load("clf.pkl")

    def fit(self, database, target):
        self.clf.fit(database, target)


def generate_database(count):
    temp = [[], []]
    for _ in range(count):
        temp[0].append((randint(-100, 100), randint(-100, 100)))
        temp[1].append(temp[0][-1][0] + temp[0][-1][1])
    return temp


def check_acc(neur, database):
    temp = 0
    for i in range(len(database[0])):
        if ceil(neur.predict([database[0][i]])) == database[1][i]:
            temp += 1
    return temp / len(database[0])


mlp = MlpNet()
database = generate_database(10000)
mlp.fit(database[0], database[1])
print(check_acc(mlp, generate_database(10000)))
