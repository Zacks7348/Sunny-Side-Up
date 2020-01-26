"""
Sunny Side Up

Date Modified:  January 26, 2020
Author: Zacks7348, Lvis47, Lfigu042
"""

import pandas as pd


def fetch_data(filename, city, year=None):
    """
    Extracts data from csv files by filename, city, and year
    :param filename: csv file to pull data from
    :param city: choose which city's data to extract
    :param year: choose which year's data to extract
    :return: data pandas.DataFrame
    """
    filename = "kaggle/{}.csv".format(filename)
    data = pd.read_csv(filename, usecols=["datetime", city], infer_datetime_format=True, na_values=" NaN")
    if year is None:
        return data
    data = data[data["datetime"].str.contains(str(year))]
    data = data[~data["datetime"].str.contains("02-29")]
    return data

def get_cities():
    """
    Fetch list of cities from dataset
    :return: list of cities
    """
    data = pd.read_csv("kaggle/city_attributes.csv", usecols=["City"])
    return data[data.columns[0]].to_list()
