# Series / Parallel combination calculator
#
# This file contains the GUI for the spCombCalc.
# User can input a target value and select a target e-series of preferred values, tool will find closest value as well
# as calculate closest series and parallel combinations with deviation from target value.
#
# GUI needs ttkthemes installed !
#
# !!! WIP !!!
# This tool is meant to be a simple test for setting up GUIs in Python, here with Tkinter and TTK.
# It is neither finished nor optimized, but fully working without major bugs, as far as testing showed.
# For questions, advice or further info, please visit:
#
# github.com/BorisJung/SeriesParallelCombinationCalculator
#
#
#
#
# Version: 0.1
#
# Author: Boris Jung
# Date: 22.03.2020
#
#
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

from spComb_calc___v0_1 import calc_spc


def calculate(*args):
    try:
        value = float(targVal.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def validValue(*args):
    try:
        #print(valEx_Label.keys())
        float(targVal.get())
        tVal_Label.config(foreground=ttk.Style().lookup("TLabel", "foreground"))
        valEx_Label.config(foreground=ttk.Style().lookup("TLabel", "foreground"))
    except ValueError:
        tVal_Label.config(foreground='red')
        valEx_Label.config(foreground='red')

def targSeriesUpdate(*args):
    targSeries = comboExample



def update_spc_vals(*args):
    validValue()
    returnValues = calc_spc(targVal.get(), targSeries.get())
    cVal.set(returnValues["cVal"]); cDev.set("{}%".format(returnValues["cDev"]))
    sComb.set(returnValues["sComb"]); sDev.set("{}%".format(returnValues["sDev"]))
    sVal1.set(returnValues["sVal1"]); sVal2.set(returnValues["sVal2"])
    pComb.set(returnValues["pComb"]); pDev.set("{}%".format(returnValues["pDev"]))
    pVal1.set(returnValues["pVal1"]); pVal2.set(returnValues["pVal2"])

def update_spc_val(*args):
    print(targVal.get())
    print(type(targVal.get()))
    print(targSeries.get())
    print(type(targSeries.get()))


#
#
#____________________________________________________________________________________________________________________
# Window and Theme
root = Tk() # Create window
root.title("series / parallel combination calculator") # Set window title
# Setting theme
style = ThemedStyle(root)
style.set_theme("arc")
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Frame creation
mainframe = ttk.Frame(root, padding="3 3 12 12") # Create frame with padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # Set fram to window size (?)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Variables
targVal = StringVar()
valExample = StringVar()
valExample.set("(e.g. 1247 or 1.247e3)")
targSeries = StringVar()
meters = StringVar()
cVal = StringVar(); cDev = StringVar()
sComb = StringVar(); sVal1 = StringVar(); sVal2 = StringVar(); sDev = StringVar()
pComb = StringVar(); pVal1 = StringVar(); pVal2 = StringVar(); pDev = StringVar()
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Header
ttk.Label(mainframe, text="Series/Parallel combination calculator",
          font=("Verdana", 24)).grid(column=1, row=1, columnspan=4, sticky=(W, E))
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Target value input textbox
tVal_Label = ttk.Label(mainframe, text="Target value")
tVal_Label.grid(column=1, row=2, sticky=W)
tVal_entry = ttk.Entry(mainframe, width=7, textvariable=targVal)
tVal_entry.grid(column=2, row=2, sticky=(W, E)) # doesnt work in single line with above entry definition
valEx_Label = ttk.Label(mainframe, textvariable=valExample)
valEx_Label.grid(column=3, row=2, sticky=W)
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Target series dropdown menu
ttk.Label(mainframe, text="E-Series").grid(column=1, row=3, sticky=W)
comboExample = ttk.Combobox(mainframe, state="readonly",
                            values=["E3","E6","E12","E24","E48","E96","E192"])
comboExample.grid(column=2, row=3)
comboExample.current(1)
targSeries = comboExample
comboExample.bind("<<ComboboxSelected>>", targSeriesUpdate)
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Button
ttk.Button(mainframe, text="Calculate", command=update_spc_vals).grid(column=1, row=4, columnspan=3, sticky=(W, E))
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Results
ttk.Label(mainframe, text="Results", font=("Verdana", 24)).grid(column=1, row=5, sticky=W)
#____________________________________________________________________________________________________________________
# Closes Value
ttk.Label(mainframe, text="Closest single value:").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, background="white",
          textvariable=cVal).grid(column=3, row=6, sticky=(W, E))
ttk.Label(mainframe, text="Deviation from target value: ").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, textvariable=cDev).grid(column=3, row=7, sticky=(E))
#____________________________________________________________________________________________________________________
# Series Value
ttk.Label(mainframe, text="Series combination:").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, background="white",
          textvariable=sComb).grid(column=3, row=8, sticky=(W, E))
ttk.Label(mainframe, text="Deviation from target value: ").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, textvariable=sDev).grid(column=3, row=9, sticky=(E))
ttk.Label(mainframe, text="Values: ").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, textvariable=sVal1).grid(column=2, row=10, sticky=W)
ttk.Label(mainframe, textvariable=sVal2).grid(column=3, row=10, sticky=W)
#____________________________________________________________________________________________________________________
# Parallel Value
ttk.Label(mainframe, text="Parallel combination:").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, background="white",
          textvariable=pComb).grid(column=3, row=11, sticky=(W, E))
ttk.Label(mainframe, text="Deviation from target value: ").grid(column=1, row=12, sticky=W)
ttk.Label(mainframe, textvariable=pDev).grid(column=3, row=12, sticky=(E))
ttk.Label(mainframe, text="Values: ").grid(column=1, row=13, sticky=W)
ttk.Label(mainframe, textvariable=pVal1).grid(column=2, row=13, sticky=W)
ttk.Label(mainframe, textvariable=pVal2).grid(column=3, row=13, sticky=W)
#____________________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________________
# Additional settings
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5) # Add padding between widgets
#
tVal_entry.focus() # Set cursor focus to tVal_entry text input box
root.bind('<Return>', update_spc_vals) # Bind RETURN key to calculate function/button
#
#____________________________________________________________________________________________________________________
root.mainloop()
#____________________________________________________________________________________________________________________