import json

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
    
