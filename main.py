from gui.gui import run
from data import fetch_data
import plotter as p

#Takes in user input and plots data

year1, dataset, city, year2 = run()
'''
x = []
y = []
years = []
years.append(year1)
years.append(year2)
data1 = fetch_data(dataset, city, years[0])
data2 = fetch_data(dataset, city, years[1])
temp1, temp2 = p.create_axes(data1, dataset)
x.append(temp1)
y.append(temp2)
temp1, temp2 = p.create_axes(data2, dataset)
x.append(temp1)
y.append(temp2)

p.graph(x, y, years, dataset, city)
'''

data1 = fetch_data(dataset, city, year1)
data2 = fetch_data(dataset, city, year2)
x1, y1 = p.create_axes(data1, dataset)
x2, y2 = p.create_axes(data2, dataset)
p.graph(x1, x2, y1, y2, year1, year2, dataset, city)



