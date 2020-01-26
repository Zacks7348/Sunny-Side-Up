import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from utils import parse_datetime, kelvin_to_farenheit, average_list

def create_axis(data, data_type):
    '''
    x = data[data.columns[0]].to_list()
    for date in x:
        x[x.index(date)] = parse_datetime(date)  
    y = data[data.columns[1]].to_list()
    for value in y:
        y[y.index(value)] = float("{:.2f}".format(kelvin_to_farenheit(value)))
    return x, y
    '''
    data_x = data[data.columns[0]].to_list()
    data_y = data[data.columns[1]].to_list()
    output = {}
    if data_type == "temperature":
        for i in range(0, len(data_x)):
            date = parse_datetime(data_x[i])
            if date in output.keys():
                output[date].append(kelvin_to_farenheit(data_y[i]))
            else:
                output[date] = [kelvin_to_farenheit(data_y[i])]
    for key in output.keys():
        output[key] = average_list(output[key])
    return list(output.keys()), list(output.values())

#Generates graph for passed data
def graph(title, xlabel, ylabel, xdata, ydata):
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.plot(xdata, ydata)
    plt.show()