"""
Sunny Side Up

Date Modified:  January 26, 20202
Author: Zacks7348, Lvis47, Lfigu042
"""

from tkinter import * #@unusedImports
from tkinter import ttk
from data import get_cities #import city list from data.py which pulls from dataset 
from tkinter.simpledialog import Dialog
from PIL import Image, ImageTk #for image input
import inspect
import asyncio

class ComboBoxDemo(ttk.Frame): 
    """
    Represents GUI window. Main class for all frame data
    """  
    def __init__(self, isapp=True, name='ssu'):
        """
        Initializes GUI window
        :param isapp: sets isapp
        :param name: sets name of window
        """
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('From Miami with Love')
        self.isapp = isapp
        self._create_widgets()
   
    def get_inputs(self):
        """
        Returns values from drop-down inputs
        :return: 4 Strings; year1, dataset, city, year2
        """
        return self.cb1.get(), self.cb2.get(), self.cb3.get(), self.cb4.get()

    def _create_widgets(self):
        """
        Wrapper method for creating necessary widgets
        """
        if self.isapp:
            frontPage(self, "gui\SSUlogo1.png") # import and set image to frame

            buttons(self) # create and define(w/information) buttons
        
        self._create_demo_panel()
   
    def _create_demo_panel(self):
        """
        Generates frame to be displayed on window.
        Creates all drop-down inputs
        """
        panel = Frame(self)
        panel.pack(side=TOP, fill=BOTH, expand=Y) #resize with parent frame
            
        # 1st combobox, fixed year values
        years = ('2013', '2014', '2015', '2016', '2017')
        cbp1 = ttk.Labelframe(panel, text='Select 2 years to compare')
        self.cb1 = ttk.Combobox(cbp1, values=years, state='readonly')
        self.cb1.pack(pady=5, padx=10)

        # 4th combobox, fixed year values
        cbp4 = ttk.Labelframe(panel, text='Year')
        self.cb4 = ttk.Combobox(cbp1, values=years, state='readonly')
        self.cb4.pack(pady=5, padx=10)
        
        # 2nd combobox, fixed values for data type 
        data = ('Humidity', 'Pressure', 'Temperature')
        cbp2 = ttk.Labelframe(panel, text='Desired Data')
        self.cb2 = ttk.Combobox(cbp2, values=data, state='readonly')
        self.cb2.pack(pady=5, padx=10)

        # 3rd combobox, gets city list from Dataset
        cities = (get_cities())
        cbp3 = ttk.Labelframe(panel, text='Cities')
        self.cb3 = ttk.Combobox(cbp3, values=cities, state='readonly')
        self.cb3.pack(pady=5, padx=10)

        # position and display
        cbp1.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp2.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp3.pack(in_=panel, side=TOP, pady=5, padx=10)
        cbp4.pack(in_=panel, side=TOP, pady=5, padx=10)
     
class frontPage(ttk.Frame):
    """
    Image Handler for window
    """
    def __init__(self, master, filename):
        """
        Initializes image to be displayed on window
        :param master: top-level window to display information
        :param filename: path to image
        """
        ttk.Frame.__init__(self, master)
        self.master = master
        self.pack(side=TOP, fill=X)
        
        load = Image.open(filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=100)
        img.pack(fill=X,padx=5,pady=5)
               
class buttons(ttk.Frame):
    """
    Represents interactive buttons in window
    """
    def __init__(self, master):
        """
        Initializes buttons
        :param master: top-level window
        """
        ttk.Frame.__init__(self, master)
        self.pack(side=BOTTOM, fill=X)
         
        sep = ttk.Separator(orient=HORIZONTAL)
 
        # Function of Exit button
        dismissBtn = ttk.Button(text='Exit', command=self.master.quit)

        # Function of see Data button
        codeBtn = ttk.Button(text='See Data', command=self.master.quit)
        codeBtn.focus()
                 
        # position widgets in frame
        sep.grid(in_=self, row=0, columnspan=4, sticky=EW, pady=5)
        codeBtn.grid(in_=self, row=1, column=0, sticky=E)
        dismissBtn.grid(in_=self, row=1, column=1, sticky=E)
         
        # set resize constraints
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
 
        # bind Escape to quit program
        self.winfo_toplevel().bind('<Escape>', quit )

def run():
    """
    Executes GUI window
    :return: inputs from GUI (ComboBoxDemo.get_inputs())
    """
    root = Tk()
    my_gui = ComboBoxDemo(root)
    root.mainloop()
    return my_gui.get_inputs()

