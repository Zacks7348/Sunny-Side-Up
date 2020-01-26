"""
Sunny Side Up

Date Modified:  January 26, 2020
Author: Zacks7348, Lvis47, Lfigu042
"""

import json
import numpy as np

def kelvin_to_farenheit (temp):
    """
    Converts Kelvin to Farenheit
    :param temp: kelvin input
    :return: Farenheit output
    """
    return float("{:.2f}".format(((temp-273.1)/5)*9+32))

def parse_datetime(datetime):
    """
    Formats datetime to abbreviated dates (01-01 -> Jan 01)
    :param datetime: datetime
    :return: abbreviated date
    """
    months = {}
    with open("dates.json", "r") as months_file:
        months = json.load(months_file)
    return "{} {}".format(months["Months"][datetime[5:7]], datetime[8:10])

def average_list(list):
    """
    Returns average of all values in list
    :param list: list of values to be averaged
    :return: average of values in list
    """
    sum = 0
    for i in list:
        sum+=i
    return float("{:.2f}".format(sum/len(list)))

def pad_floats(n):
    """
    Formats numbers to two decimal places
    :param n: number to be formatted
    :return: formatted number
    """
    return float("{:.2f}".format(n))

def average_days(dates, data, data_type):
    """
    Takes in data per hour and averages by day
    :param dates: dates from data
    :param data: values to be averaged
    :param data_type: type of data being averaged
    :return: 2 lists, dates and averaged values
    """
    def parse_data(value, data_type):
        if data_type == "temperature":
            return kelvin_to_farenheit(value)
        return pad_floats(value)
    output = {}
    for i in range(0, len(dates)):
        date = parse_datetime(dates[i])
        if date in output.keys():
            output[date].append(parse_data(data[i], data_type))
        else:
            output[date] = [parse_data(data[i], data_type)]
    for key in output.keys():
        output[key] = average_list(output[key])
    return list(output.keys()), list(output.values())



    
