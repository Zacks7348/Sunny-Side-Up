import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from utils import parse_datetime, kelvin_to_farenheit, average_list, pad_floats

def create_axes(data, data_type):
    def parse_data(value, data_type):
        if data_type == "Temperature":
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
def graph(x1, x2, y1, y2, year1, year2, dataset, city):
    fig, ax = plt.subplots()
    if dataset == "Temperature":
        plt.title("Temperature's in {}: {}".format(city, year1+" & "+year2))
        ax.set_ylabel("Temperature (F)")
    elif dataset == "Humidity":
        plt.title("Humidity in {}: {}".format(city, year1+" & "+year2))
        ax.set_ylabel("Humidity (water vapor g/m^3 of air)")
    elif dataset == "Pressure":
        plt.title("Air Pressure in {}: {}".format(city, year1+" & "+year2))
        ax.set_ylabel("Pressure (Pa)")
    ax.set_xlabel("Dates")
    ax.plot(x1, y1, color = "blue", label=year1)
    ax.plot(x2, y2, color = "red", label=year2)
    ax.legend()
    majors = []
    minors = []
    for date in x1:
        if "01" in date:
            majors.append(x1.index(date))
        else:
            minors.append(x1.index(date))

    ax.xaxis.set_major_locator(ticker.FixedLocator(majors))
    ax.xaxis.set_minor_locator(ticker.FixedLocator(minors))
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.20)
    plt.show()


