from data import fetch_data
import plotter as p

#TODO
# USER-INTERFACE FOR RECEIVING INPUTS
# GRAPH DATA/SAVE GRAPH
# PREDICT ???
# ACCEPT AWARDS AND GTFO OUT OF HERE

data = fetch_data("temperature", "Miami", 2015)
x, y = p.create_axis(data, "temperature")

p.graph("Temperatures in Miami: 2015", "Dates", "Temperatures (F)", x, y)
