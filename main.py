import requests
from sklearn import datasets, svm
from time import sleep
from sklearn.neural_network import MLPClassifier, MLPRegressor
from random import randint
import joblib
from openpyxl import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
matplotlib.use('TkAgg')


def ceil(a):
    if a >= 0:
        return int(a + 0.5)
    return int(a - 0.5)


class MlpNet:  # Regressor/Classifier
    def __init__(self):
        self.mlp = MLPRegressor(hidden_layer_sizes=(10, 5), alpha=1, max_iter=1000, power_t=0.5 * 10, tol=0.0001)

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


def generate_database(name):
    col_names = [chr(i) for i in range(65, 91)] + [j + h for j in [chr(i) for i in range(65, 91)] for h in
                                                   [chr(i) for i in range(65, 91)]]
    columns = []
    columns_names = dict()
    columns_letters = dict()

    wb = load_workbook(f"C:/Users/rezon/Downloads/{name}")["Sheet 1"]
    i = 0
    while wb[col_names[i]][0].value is not None:
        columns.append([j.value for j in wb[col_names[i]]])
        i += 1
    columns_names = {i[0]: i[1:] for i in columns}
    columns = [i[1:] for i in columns]
    columns_letters = {col_names[i]: columns[i] for i in range(len(columns))}
    useful = ["A", "C", "E", "F", "G", "M", "R", "U", "AE", "AF", "AG", "AU", "AV", "AW", "BE", "BI",
              "BL", "BW", "BY", "CA", "CB", "CC", "CD"]

    data = []
    values = []
    for i in range(len(columns_letters["A"])):
        if columns_letters["ED"][i] is not None:
            data.append([columns_letters[key][i] for key in useful])
            values.append(columns_letters["ED"][i])
    return [data, values]


def check_acc(neur, database):
    temp = 0
    for i in range(len(database[0])):
        if abs(ceil(neur.predict([database[0][i]])) - database[1][i]) < 6:
            temp += 1
        elif False:
            print(neur.predict([database[0][i]]), "\t", database[1][i], "|\t", "".join([str(int(x)) for x in database[0][i]]))
    return temp / len(database[0])


mlp = MlpNet()
data1 = generate_database("htqnbyu + result2021.xlsx")
data2 = generate_database("result2015_raex.xlsx")
data3 = generate_database("rating.xlsx")
for _ in range(500):
    print(_)
    mlp.fit(data1[0], data1[1])
    mlp.fit(data2[0], data2[1])
    mlp.fit(data3[0], data3[1])
sleep(0.3)
temp1 = check_acc(mlp, data1)
temp2 = check_acc(mlp, data2)
temp3 = check_acc(mlp, data3)
print(temp1, temp2, temp3)
"""mlp.save()
print("SAVED")
"""