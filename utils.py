def check_month(datetime, month):
    return datetime[5:7] == month

def kelvin_to_farenheit (temp):
    return float("{:.2f}".format(((temp-273.1)/5)*9+32))