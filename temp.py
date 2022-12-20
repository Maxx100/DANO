"""from bs4 import BeautifulSoup
import bs4
import requests

a = []
cnt = 1
for i in range(10):
    r = requests.get(f"https://www.webometrics.info/en/europe/russian%20federation?page={i}")
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('tr'):
        if "<tr class=\"odd\"><td><center>" in str(link) or "<tr class=\"even\"><td><center>" in str(link):
            a.append([cnt])
            cnt += 1
            a[-1] += [link.a.get("href"), link.a.getText()]
print(a)
"""

from bs4 import BeautifulSoup
import bs4
import requests
from openpyxl import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

rating = []
cnt = 1
for i in range(10):
    r = requests.get(f"https://www.webometrics.info/en/europe/russian%20federation?page={i}")
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('tr'):
        if "<tr class=\"odd\"><td><center>" in str(link) or "<tr class=\"even\"><td><center>" in str(link):
            rating.append([cnt])
            cnt += 1
            rating[-1] += [link.a.get("href"), link.a.getText()]
#print(rating)

col_names = [chr(i) for i in range(65, 91)]+[j+h for j in [chr(i) for i in range(65, 91)] for h in [chr(i) for i in range(65, 91)]]
columns = []
columns_names = dict()
columns_letters = dict()

wb = load_workbook("C:/Users/rezon/Downloads/result2022.xlsx")["Sheet 1"]
i = 0
while wb[col_names[i]][0].value != None:
    columns.append([j.value for j in wb[col_names[i]]])
    i+=1
columns_names = {i[0]: i[1:] for i in columns}
columns = [i[1:] for i in columns]
columns_letters = {col_names[i]:columns[i] for i in range(len(columns))}
rows = [[col[ind] for col in columns] + [None] for ind in range(len(columns[0]))]

q = set()
check = []
for i in rows:
    check.append(i[130].replace("https://", "").replace("http://", ""))
for row in rows:
    for ind in rating:
        try:
            if (str(row[127]).find(ind[2].split(" / ")[1]) != -1) or\
                    (ind[1].replace("https://", "").replace("http://", "") in check):
                q.add(str(row[127]))
                sheet = wb["Sheet 1"]
                exit(0)
            else:
                print(ind[1], str(row[130]))
        except IndexError:
            pass
print(len(q))
