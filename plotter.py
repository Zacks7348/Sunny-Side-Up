import os
import numpy as np 
import pandas as pd

from utils import check_month
# filepath: list, include the path of the csv datafile
filepath = []

for dirname, _, filenames in os.walk('kaggle/'):
    for filename in filenames:
        filepath.append(os.path.join(dirname, filename))

#Prints data of passed city
def graph(csv_file, city):
    data = pd.read_csv(csv_file)
    print(data[["datetime", city]])

graph("kaggle/temperature.csv", "Vancouver")
    