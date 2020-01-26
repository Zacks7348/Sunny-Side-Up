from gui.gui import run
from data import fetch_data
import plotter as p

#Takes in user input and plots data

year, dataset, city = run()
x = []
y = []
years = []
years.append(year)
years.append(str(int(year)+1))
data1 = fetch_data(dataset, city, years[0])
data2 = fetch_data(dataset, city, years[1])
temp1, temp2 = p.create_axes(data1, dataset)
x.append(temp1)
y.append(temp2)
temp1, temp2 = p.create_axes(data2, dataset)
x.append(temp1)
y.append(temp2)
p.graph(x, y, years, dataset, city)




