from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

from data import fetch_data, fetch_regression_data
from plotter import create_axes, graph_regression
from utils import map_dates

def linear_model(city, year, data=None, dataset=None):
    if data is None:
        X, y = fetch_regression_data(dataset, city, year)
    mapped_X = np.asarray(map_dates(X)).reshape(-1, 1)
    for i in mapped_X
    lin = LinearRegression()
    lin.fit(mapped_X, y)
    graph_regression(mapped_X, y, dataset, lin)

def polynomial_model(city, year, data=None, dataset=None):
    if data is None:
        data = fetch_data(dataset, city, year)
    x, y = create_axes(data, dataset)
    poly = PolynomialFeatures(degree = 4)
    x_poly = poly.fit_transform(x)
    poly.fit(x_poly, y)
    lin = LinearRegression()
    lin.fit(x_poly, y)




    
