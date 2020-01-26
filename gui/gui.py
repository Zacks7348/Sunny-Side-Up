from tkinter import *
from tkinter import ttk
from data import get_cities
from tkinter.simpledialog import Dialog
from PIL import Image, ImageTk
import inspect

class ComboBoxDemo(ttk.Frame):
    
    def __init__(self, isapp=True, name='comboboxdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Combobox Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def get_inputs(self):
        return self.cb1.get(), self.cb2.get(), self.cb3.get()

    def _create_widgets(self):
        if self.isapp:
            mainPanel(self, 
                     ["Sunny Side UP! ",
                      "",
                      "We have DataSets on 37 different cities, from 2013-2017 ",
                      "The data includes humidity, pressure and temperature. ",
                      "From the drop down below please select the desired information",
                      "Output will be compiled into a graph "])

            buttons(self)
        
        self._create_demo_panel()
        
    def _create_demo_panel(self):
        panel = Frame(self)
        panel.pack(side=TOP, fill=BOTH, expand=Y)
            
        # create comboboxes
        years = ('2013', '2014', '2015', '2016', '2017')
        cbp1 = ttk.Labelframe(panel, text='Year')
        self.cb1 = ttk.Combobox(cbp1, values=years, state='readonly')
        self.cb1.pack(pady=5, padx=10)
        
        data = ('Humidity', 'Pressure', 'Temperature')
        cbp2 = ttk.Labelframe(panel, text='Desired Data')
        self.cb2 = ttk.Combobox(cbp2, values=data, state='readonly')
        self.cb2.pack(pady=5, padx=10)

        cities = (get_cities())
        cbp3 = ttk.Labelframe(panel, text='Cities')
        self.cb3 = ttk.Combobox(cbp3, values=cities, state='readonly')
        self.cb3.pack(pady=5, padx=10)

        # position and display
        cbp1.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp2.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp3.pack(in_=panel, side=TOP, pady=5, padx=10)
    
class mainPanel(ttk.Frame):
    def __init__(self, master, msgtxt):
        ttk.Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
         
        msg = Label(self, wraplength='4i', justify=LEFT)
        msg['text'] = ''.join(msgtxt)
        msg.pack(fill=X, padx=5, pady=5)
         
class buttons(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack(side=BOTTOM, fill=X)          # resize with parent
         
        # separator widget
        sep = ttk.Separator(orient=HORIZONTAL)
 
        # Dismiss button
        dismissBtn = ttk.Button(text='Exit', command=self.master.quit)
        dismissBtn['compound'] = LEFT           # display image to left of label text

        # 'See Code' button
        codeBtn = ttk.Button(text='See Data', command=self.master.quit)
        codeBtn['compound'] = LEFT
        #codeBtn = 
        codeBtn.focus()
                 
        # position and register widgets as children of this frame
        sep.grid(in_=self, row=0, columnspan=4, sticky=EW, pady=5)
        codeBtn.grid(in_=self, row=1, column=0, sticky=E)
        dismissBtn.grid(in_=self, row=1, column=1, sticky=E)
         
        # set resize constraints
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
 
        #bind <Return> to demo window, activates 'See Code' button;
        #<'Escape'> activates 'Dismiss' button
        self.winfo_toplevel().bind('<Escape>', quit )
 


def run():
    root = Tk()
    my_gui = ComboBoxDemo(root)
    root.mainloop()
    return my_gui.get_inputs()
