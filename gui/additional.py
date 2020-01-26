from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import Dialog
from PIL import Image, ImageTk
import inspect
 
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
        codeBtn = ttk.Button(text='See Data')
        codeBtn['compound'] = LEFT
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
        self.winfo_toplevel().bind('<Return>', lambda x: codeBtn.invoke() )
        self.winfo_toplevel().bind('<Escape>', quit )
 
