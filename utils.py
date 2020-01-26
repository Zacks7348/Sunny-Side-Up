import json
import numpy as np

def kelvin_to_farenheit (temp):
    return float("{:.2f}".format(((temp-273.1)/5)*9+32))

def parse_datetime(datetime):
    months = {}
    with open("dates.json", "r") as months_file:
        months = json.load(months_file)
    return "{} {}".format(months["Months"][datetime[5:7]], datetime[8:10])

def average_list(list):
    sum = 0
    for i in list:
        sum+=i
    return float("{:.2f}".format(sum/len(list)))

def pad_floats(n):
    return float("{:.2f}".format(n))

def map_dates(dates):
    mapped_values = dates
    for i in range(0, len(dates)):
        mapped_values[i] = i
    return mapped_values

def average_days(dates, data, data_type):
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



    
