import pandas as pd

class DataType():
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    PRESSURE = "Pressure"

def fetch_data(filename, city, year=None):
    filename = "kaggle/{}.csv".format(filename)
    data = pd.read_csv(filename, usecols=["datetime", city], infer_datetime_format=True, na_values=" NaN")
    if year is None:
        return data
    data = data[data["datetime"].str.contains(str(year))]
    data = data[~data["datetime"].str.contains("02-29")]
    return data

def get_cities():
    data = pd.read_csv("kaggle/city_attributes.csv", usecols=["City"])
    return data[data.columns[0]].to_list()
