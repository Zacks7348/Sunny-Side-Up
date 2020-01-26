import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from utils import parse_datetime, kelvin_to_farenheit, average_list, pad_floats

def create_axes(data, data_type):
    def parse_data(value, data_type):
        if data_type == "temperature":
            return kelvin_to_farenheit(value)
        return pad_floats(value)
    data_x = data[data.columns[0]].to_list()
    data_y = data[data.columns[1]].to_list()
    output = {}
    for i in range(0, len(data_x)):
        date = parse_datetime(data_x[i])
        if date in output.keys():
            output[date].append(parse_data(data_y[i], data_type))
        else:
            output[date] = [parse_data(data_y[i], data_type)]
    for key in output.keys():
        output[key] = average_list(output[key])
    return list(output.keys()), list(output.values())

#Generates graph for passed data
def graph(xdata=[], ydata=[], year=[], dataset=None, city=None):
    fig, ax = plt.subplots()
    if dataset == "Temperature":
        plt.title("Temperature's in {}: {}".format(city, year[0]+" & "+year[1]))
        ax.set_ylabel("Temperature (F)")
    elif dataset == "Humidity":
        plt.title("Humidity in {}: {}".format(city, year[0]+" & "+year[1]))
        ax.set_ylabel("Humidity (water vapor g/m^3 of air)")
    elif dataset == "Pressure":
        plt.title("Air Pressure in {}: {}".format(city, year[0]+" & "+year[1]))
        ax.set_ylabel("Pressure (Pa)")
    ax.set_xlabel("Dates")
    ax.plot(xdata[0], ydata[0], color = "blue", label=year[0])
    ax.plot(xdata[1], ydata[1], color = "red", label=year[1])
    ax.legend()
    majors = []
    minors = []
    for date in xdata[0]:
        if "01" in date:
            majors.append(xdata[0].index(date))
        else:
            minors.append(xdata[0].index(date))

    ax.xaxis.set_major_locator(ticker.FixedLocator(majors))
    ax.xaxis.set_minor_locator(ticker.FixedLocator(minors))
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.20)
    plt.show()


