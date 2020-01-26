from data import fetch_data
import plotter as p

#TODO
# USER-INTERFACE FOR RECEIVING INPUTS
# GRAPH DATA/SAVE GRAPH
# PREDICT ???
# ACCEPT AWARDS AND GTFO OUT OF HERE

dataset = input("Enter dataset: ")
city = input("Enter city: ")
year = input("Enter year: ")

data = fetch_data(dataset, city, year)
x, y = p.create_axis(data, "temperature")

p.graph(x, y, dataset, city, year)
