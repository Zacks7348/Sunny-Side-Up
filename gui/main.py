from tkinter import *
from tkinter import ttk

from additional import MsgPanel,SeeDismissPanel

class ComboBoxDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='comboboxdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Combobox Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["Sunny Side UP! ",
                      "",
                      "We have DataSets on 37 different cities, from 2013-2017 ",
                      "The data includes humidity, pressure and temperature. ",
                      "From the drop down below please select the desired information",
                      "Output will be compiled into a graph "])

            SeeDismissPanel(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        panel = Frame(self)
        panel.pack(side=TOP, fill=BOTH, expand=Y)
            
        # create comboboxes
        years = ('2013', '2014', '2015', '2016', '2017')
        cbp1 = ttk.Labelframe(panel, text='Based on data')
        cb1 = ttk.Combobox(cbp1, values=years, state='readonly')
        #cb1.bind('<Return>', self._update_values)
        cb1.pack(pady=5, padx=10)
        
        data = ('Humidity', 'Pressure', 'Temperature')
        cbp2 = ttk.Labelframe(panel, text='Based on data')
        cb2 = ttk.Combobox(cbp2, values=data, state='readonly')
        cb2.current(1)  # set selection
        cb2.pack(pady=5, padx=10)

        cities = ('Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John')
        cbp3 = ttk.Labelframe(panel, text='Based on data')
        cb3 = ttk.Combobox(cbp3, values=cities, state='readonly')
        cb3.current(1)  # set selection
        cb3.pack(pady=5, padx=10)

        # position and display
        cbp1.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp2.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp3.pack(in_=panel, side=TOP, pady=5, padx=10)

root = Tk()
my_gui = ComboBoxDemo(root)
root.mainloop()