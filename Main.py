""""

This is the code for main window which cross-reference Joback_Hand_Pick.py and Joback_Smiles.py
The code is written by Chenyang Shi at AbbVie.
Send him an email at chenyang.shi@abbvie.com for questions and suggestions. 

"""

from tkinter import *
from tkinter import ttk
from math import exp
import tkinter as tk
#from FaCS import FaCS
from Joback_Hand_Pick import Hand_Pick
from Joback_Smiles import Auto_Search
import os  # for loading files or exporting files


class Overall_Look:
    def __init__(self, master):
        self.master = master
        self.master.title("Joback & Reid GUI")
        self.master.configure(background = "#add8e6") #the color will be changed later
        self.master.minsize(800, 300) # width + height
        self.master.resizable(False, False)


##define style in ttk##
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#add8e6')
        self.style.configure('TButton', background = '#add8e6')
        self.style.configure('TLabel', background = '#add8e6', font = ('Arial', 12))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        
##load image##
        self.logo = PhotoImage(file = "molecule.gif").subsample(5,5)

##this is the top frame, we will write a few sentences about this program##
        self.frame_header = ttk.Frame(master, relief = RIDGE, padding = (30, 15))
        self.frame_header.pack()

        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = "w")
        ttk.Label(self.frame_header, text = 'Welcome to use Joback & Reid GUI program!',
                  style = 'Header.TLabel').grid(row = 0, column = 2, columnspan = 4)
        ttk.Label(self.frame_header, wraplength = 600,
                  text = ("This program predicts eleven physical properties of a given molecular structre via group "
                          "contribution method proposed by Joback and Reid (Chem. Eng. Comm. 1987, 57, 233-243). " 
                          "The program runs in two modes--manual and auto modes. In manual mode, the users can "
                          "select and specify the types/numbers of functional groups of a molecule. While in auto mode, both "
                          "parameters can be detected automatically if a SMILES string of the molecule is given. "
                          "Also in auto mode, users can process molecules in a batch mode by loading SMILES codes in a txt file."
                          "The predicted properties along with 200+ molecular descriptors will be saved into a csv file."
                          )).grid(row = 1, column = 2, columnspan = 4)
        

        self.bottom_frame = ttk.Frame(master, relief = FLAT, padding = (30, 15)) 
        self.bottom_frame.pack()
        
        Button(self.bottom_frame, text = 'Manually Select Functional Groups', relief = RAISED,
                    command = self.hand_pick, font = ('Arial', 14, "bold")).grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)
        Button(self.bottom_frame, text = 'Auto-Detect Groups via SMILES', relief = RAISED,
                    command = self.smiles, font = ('Arial', 14, "bold")).grid(row = 0, column = 3, columnspan = 3, padx = 5, pady = 5)
        
    def hand_pick(self):
        self.hand_pick = tk.Toplevel(self.master)
        self.GUI = Hand_Pick(self.hand_pick)   
        

    def smiles(self):
        self.smiles = tk.Toplevel(self.master)
        self.GUI = Auto_Search(self.smiles)


def main():
    root = Tk()
    GUI = Overall_Look(root)
    root.mainloop()

if __name__ == "__main__": main()
