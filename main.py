from data import fetch_data, get_cities
import plotter as p

from regression.models import linear_model

'''
dataset = input("Enter dataset: ")
city = input("Enter city: ")
year = input("Enter year: ")
'''
dataset = "Temperature"
city = "Miami"
year = 2017

data = fetch_data(dataset, city, year)
'''
x, y = p.create_axes(data, dataset)
p.graph(x, y, dataset, city, year)
'''
#linear_model(city, year, data=None, dataset=dataset)

print(get_cities())
