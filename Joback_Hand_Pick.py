""""

Here are the code for manually selecting functional groups in Joback and Reid method.
The code is written by Chenyang Shi at AbbVie.
Send him an email at chenyang.shi@abbvie.com for questions and suggestions. 

"""
from tkinter import *
from tkinter import ttk
import math


class Hand_Pick:

    def __init__(self, master):

        self.master = master
        self.master.title('Prediction of Physical Properties of Druglike Molecule--Manual Mode') # This will be shown in top of the main window
        self.master.minsize(900, 680)
        self.master.resizable(False, False)
        self.master.configure(background = '#add8e6') # light blue
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#add8e6')
        self.style.configure('TButton', background = '#add8e6')
        self.style.configure('TCheckbutton', background = '#add8e6')
        self.style.configure('TRadiobutton', background = '#add8e6')
        
        self.style.configure('TLabel', background = '#add8e6', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        ttk.Label(self.master, text = "This method is based on Joback and Reid, Chem. Eng. Comm. 1987, 57, 233-243.\n"
                                      "Please select type of groups by checkbuttons. Please specify the number of groups by typing in the entry box.\n"
                                      "Click Compute Physical Properties to see results. Click Reset to Default to clear results."
                                       , font = ('Arial', 12, 'bold'), justify = CENTER).pack(side  = TOP)
        
        self.top_frame = ttk.Frame(self.master, padding = (30, 15))
        self.top_frame.pack()
        ##labels
        ttk.Label(self.top_frame, text = "Non-ring increments", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row = 0,
                                            column = 0, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Ring increments", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row = 0,
                                            column = 2, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Halogen increments", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row = 0,
                                            column = 4, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Oxygen increments", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row = 0,
                                            column = 6, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Nitrogen increments", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row = 0,
                                            column = 8, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Sulfur increments", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row = 0,
                                            column = 10, columnspan = 2, padx = 5, sticky = "sw")

        ##Checkbutton
        #Non-ring increments #10
        self.var_0 = IntVar()
        self.var_1 = IntVar()
        self.var_2 = IntVar()
        self.var_3 = IntVar()
        self.var_4 = IntVar()
        self.var_5 = IntVar()
        self.var_6 = IntVar()
        self.var_7 = IntVar()
        self.var_8 = IntVar()
        self.var_9 = IntVar()
        ##Ring increments #5
        self.var_10 = IntVar()
        self.var_11 = IntVar()
        self.var_12 = IntVar()
        self.var_13 = IntVar()
        self.var_14 = IntVar()
        #Halogen increments #4       
        self.var_15 = IntVar()
        self.var_16 = IntVar()
        self.var_17 = IntVar()
        self.var_18 = IntVar()
        #Oxygen increments #10
        self.var_19 = IntVar()        
        self.var_20 = IntVar()
        self.var_21 = IntVar()
        self.var_22 = IntVar()
        self.var_23 = IntVar()
        self.var_24 = IntVar()
        self.var_25 = IntVar()
        self.var_26 = IntVar()
        self.var_27 = IntVar()
        self.var_28 = IntVar()
        #Nitrogen increments #9
        self.var_29 = IntVar()
        self.var_30 = IntVar()
        self.var_31 = IntVar()
        self.var_32 = IntVar()
        self.var_33 = IntVar()
        self.var_34 = IntVar()
        self.var_35 = IntVar()
        self.var_36 = IntVar()
        self.var_37 = IntVar()
        #Sulfur increments #3
        self.var_38 = IntVar()
        self.var_39 = IntVar()
        self.var_40 = IntVar()

###checkbutton
        ##Non-ring increments #10
        ttk.Checkbutton(self.top_frame, text = "-CH3", variable = self.var_0, style = "TCheckbutton" ).grid(row = 1,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-CH2-", variable = self.var_1).grid(row = 2,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">CH-", variable = self.var_2 ).grid(row = 3,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">C<", variable = self.var_3 ).grid(row = 4,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=CH2", variable = self.var_4 ).grid(row = 5,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=CH-", variable = self.var_5 ).grid(row = 6,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=C<", variable = self.var_6).grid(row = 7,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=C=", variable = self.var_7 ).grid(row = 8,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "#CH", variable = self.var_8 ).grid(row = 9,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "#C-", variable = self.var_9 ).grid(row = 10,
                                            column = 0, columnspan = 1, padx = 5, sticky = "sw")
        ##Ring increments #5
        ttk.Checkbutton(self.top_frame, text = "-CH2-", variable = self.var_10 ).grid(row = 1,
                                            column = 2, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">CH-", variable = self.var_11 ).grid(row = 2,
                                            column = 2, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">C<", variable = self.var_12 ).grid(row = 3,
                                            column = 2, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=CH-", variable = self.var_13 ).grid(row = 4,
                                            column = 2, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=C<", variable = self.var_14 ).grid(row = 5,
                                            column = 2, columnspan = 1, padx = 5, sticky = "sw")
        ##Halogen increments #4
        ttk.Checkbutton(self.top_frame, text = "-F", variable = self.var_15 ).grid(row = 1,
                                            column = 4, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-Cl", variable = self.var_16 ).grid(row = 2,
                                            column = 4, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-Br", variable = self.var_17 ).grid(row = 3,
                                            column = 4, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-I", variable = self.var_18 ).grid(row = 4,
                                            column = 4, columnspan = 1, padx = 5, sticky = "sw")
        ##Oxygen increments #10     
        ttk.Checkbutton(self.top_frame, text = "-OH (alcohol)", variable = self.var_19 ).grid(row = 1,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-OH (phenol)", variable = self.var_20 ).grid(row = 2,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-O- (nonring)", variable = self.var_21 ).grid(row = 3,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-O- (ring)", variable = self.var_22 ).grid(row = 4,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">C=O (nonring)", variable = self.var_23 ).grid(row = 5,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">C=O (ring)", variable = self.var_24 ).grid(row = 6,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "O=CH- (aldehyde)", variable = self.var_25 ).grid(row = 7,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-COOH (acid)", variable = self.var_26 ).grid(row = 8,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-COO- (ester)", variable = self.var_27 ).grid(row = 9,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=O (other than above)", variable = self.var_28 ).grid(row = 10,
                                            column = 6, columnspan = 1, padx = 5, sticky = "sw")
        ##Nitrogen increments #9
        ttk.Checkbutton(self.top_frame, text = "-NH2", variable = self.var_29 ).grid(row = 1,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">NH (nonring)", variable = self.var_30 ).grid(row = 2,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">NH (ring)", variable = self.var_31 ).grid(row = 3,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = ">N- (nonring)", variable = self.var_32 ).grid(row = 4,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-N= (nonring)", variable = self.var_33 ).grid(row = 5,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-N= (ring)", variable = self.var_34 ).grid(row = 6,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "=NH", variable = self.var_35 ).grid(row = 7,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-CN", variable = self.var_36 ).grid(row = 8,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-NO2", variable = self.var_37 ).grid(row = 9,
                                            column = 8, columnspan = 1, padx = 5, sticky = "sw")
        ##Sulfur increments #3
        ttk.Checkbutton(self.top_frame, text = "-SH", variable = self.var_38 ).grid(row = 1,
                                            column = 10, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-S- (nonring)", variable = self.var_39 ).grid(row = 2,
                                            column = 10, columnspan = 1, padx = 5, sticky = "sw")
        ttk.Checkbutton(self.top_frame, text = "-S- (ring)", variable = self.var_40 ).grid(row = 3,
                                            column = 10, columnspan = 1, padx = 5, sticky = "sw")    


        ##entry box
##non-ring increments
        self.N_0 = StringVar()        
        self.N_1 = StringVar()
        self.N_2 = StringVar()
        self.N_3 = StringVar()
        self.N_4 = StringVar()
        self.N_5 = StringVar()
        self.N_6 = StringVar()
        self.N_7 = StringVar()
        self.N_8 = StringVar()
        self.N_9 = StringVar()
##ring increments            
        self.N_10 = StringVar()    
        self.N_11 = StringVar()
        self.N_12 = StringVar()
        self.N_13 = StringVar()
        self.N_14 = StringVar()
##halogen incremetns         
        self.N_15 = StringVar()        
        self.N_16 = StringVar()
        self.N_17 = StringVar()
        self.N_18 = StringVar()
##oxygen increments          
        self.N_19 = StringVar()      
        self.N_20 = StringVar()
        self.N_21 = StringVar()
        self.N_22 = StringVar()
        self.N_23 = StringVar()
        self.N_24 = StringVar()
        self.N_25 = StringVar()
        self.N_26 = StringVar()
        self.N_27 = StringVar()
        self.N_28 = StringVar()
##nitrogen increments        
        self.N_29 = StringVar()
        self.N_30 = StringVar()
        self.N_31 = StringVar()
        self.N_32 = StringVar()
        self.N_33 = StringVar()
        self.N_34 = StringVar()
        self.N_35 = StringVar()
        self.N_36 = StringVar()
        self.N_37 = StringVar()
##sulfur increments        
        self.N_38 = StringVar()
        self.N_39 = StringVar()
        self.N_40 = StringVar()

####set entry default value to 0
        self.N_0.set(0)        
        self.N_1.set(0)
        self.N_2.set(0)
        self.N_3.set(0)
        self.N_4.set(0)
        self.N_5.set(0)
        self.N_6.set(0)
        self.N_7.set(0)
        self.N_8.set(0)
        self.N_9.set(0)
        self.N_10.set(0)
        self.N_11.set(0)
        self.N_12.set(0)
        self.N_13.set(0)
        self.N_14.set(0)
        self.N_15.set(0)
        self.N_16.set(0)
        self.N_17.set(0)
        self.N_18.set(0)
        self.N_19.set(0)
        self.N_20.set(0)
        self.N_21.set(0)
        self.N_22.set(0)
        self.N_23.set(0)
        self.N_24.set(0)
        self.N_25.set(0)
        self.N_26.set(0)
        self.N_27.set(0)
        self.N_28.set(0)
        self.N_29.set(0)
        self.N_30.set(0)
        self.N_31.set(0)
        self.N_32.set(0)
        self.N_33.set(0)
        self.N_34.set(0)
        self.N_35.set(0)
        self.N_36.set(0)
        self.N_37.set(0)
        self.N_38.set(0)
        self.N_39.set(0)
        self.N_40.set(0)

##add temperature, molecular weight and number of atoms
## add number of carbon atoms, number of hetero atoms and GSE choices (Radiobutton)
        self._temperature = StringVar()
        self._temperature.set(298)

        self.NoA = StringVar()
        self.NoA.set(30)

        self.MoleWeight = StringVar()
        self.MoleWeight.set(100)

        self.NoC = StringVar() ##number of carbon atoms
        self.NoC.set(15)

        self.NHET = StringVar() ##number of hetero atoms
        self.NHET.set(1)

        self.GSEradio =  IntVar()
        self.GSEradio.set(0)
        
#add a Boiling Point to it.
        self.BoilingPoint = StringVar()
        self.BoilingPoint.set("")
            
        ttk.Label(self.top_frame, text = "Temperature (K)", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row=12, column = 0, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Number of Atoms", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row=12, column = 4, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Molecule Weight (g/mol)", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row=12, column = 8, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Number of Carbon Atoms", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row=13, column = 0, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Number of Hetero Atoms", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row=13, column = 4, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Label(self.top_frame, text = "Boiling Point (K)", justify = CENTER, font = ('Arial', 12, 'bold')).grid(row=14, column = 0, columnspan = 2, padx = 5, sticky = "sw")

        ttk.Entry(self.top_frame, width = 12, font = ('Arial', 10),
                  textvariable = self._temperature).grid(row=12, column = 2, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Entry(self.top_frame, width = 12, font = ('Arial', 10),
                  textvariable = self.NoA).grid(row=12, column = 6, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Entry(self.top_frame, width = 12, font = ('Arial', 10),
                  textvariable = self.MoleWeight).grid(row=12, column = 10, columnspan = 2, padx = 5, sticky = "sw")

        ttk.Entry(self.top_frame, width = 12, font = ('Arial', 10),
                  textvariable = self.NoC).grid(row=13, column = 2, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Entry(self.top_frame, width = 12, font = ('Arial', 10),
                  textvariable = self.NHET).grid(row=13, column = 6, columnspan = 2, padx = 5, sticky = "sw")
        ttk.Entry(self.top_frame, width = 12, font = ('Arial', 10),
                  textvariable = self.BoilingPoint).grid(row=14, column = 2, columnspan = 2, padx = 5, sticky = "sw")
        
        ttk.Radiobutton(self.top_frame, text = "General Solubility Equation 1 (log S = 0.8 - logP - 0.01*(MP-25))",
                  variable = self.GSEradio, style = "TRadiobutton", value = 0).grid(row=13, column = 8, columnspan = 4, padx = 5, sticky = "sw")
        ttk.Radiobutton(self.top_frame, text = "General Solubility Equation 2 (log S = 0.5 - logP - 0.01*(MP-25))",
                  variable = self.GSEradio, value = 1).grid(row=14, column = 8, columnspan = 4, padx = 5, sticky = "sw")        
        
        self.width = 8

        self.entry_N_1 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_0)
        self.entry_N_2 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_1)
        self.entry_N_3 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_2)
        self.entry_N_4 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_3)
        self.entry_N_5 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_4)
        self.entry_N_6 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_5)
        self.entry_N_7 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_6)
        self.entry_N_8 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_7)
        self.entry_N_9 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_8)
        self.entry_N_10 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_9)
        self.entry_N_11 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_10)
        self.entry_N_12 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_11)
        self.entry_N_13 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_12)
        self.entry_N_14 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_13)
        self.entry_N_15 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_14)
        self.entry_N_16 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_15)
        self.entry_N_17 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_16)
        self.entry_N_18 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_17)
        self.entry_N_19 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_18)
        self.entry_N_20 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_19)
        self.entry_N_21 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_20)
        self.entry_N_22 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_21)
        self.entry_N_23 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_22)
        self.entry_N_24 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_23)
        self.entry_N_25 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_24)
        self.entry_N_26 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_25)
        self.entry_N_27 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_26)
        self.entry_N_28 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_27)
        self.entry_N_29 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_28)
        self.entry_N_30 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_29)
        self.entry_N_31 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_30)
        self.entry_N_32 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_31)
        self.entry_N_33 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_32)
        self.entry_N_34 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_33)
        self.entry_N_35 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_34)
        self.entry_N_36 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_35)
        self.entry_N_37 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_36)
        self.entry_N_38 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_37)
        self.entry_N_39 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_38)
        self.entry_N_40 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_39)
        self.entry_N_41 = ttk.Entry(self.top_frame, width = self.width, font = ('Arial', 10), textvariable = self.N_40)
       
##non-ring increment
        self.entry_N_1.grid(row=1, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_2.grid(row=2, column = 1, columnspan = 1, padx = 5, sticky = "sw")      
        self.entry_N_3.grid(row=3, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_4.grid(row=4, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_5.grid(row=5, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_6.grid(row=6, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_7.grid(row=7, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_8.grid(row=8, column = 1, columnspan = 1, padx = 5, sticky = "sw")      
        self.entry_N_9.grid(row=9, column = 1, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_10.grid(row=10, column = 1, columnspan = 1, padx = 5, sticky = "sw")
##ring increment        
        self.entry_N_11.grid(row=1, column = 3, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_12.grid(row=2, column = 3, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_13.grid(row=3, column = 3, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_14.grid(row=4, column = 3, columnspan = 1, padx = 5, sticky = "sw")      
        self.entry_N_15.grid(row=5, column = 3, columnspan = 1, padx = 5, sticky = "sw")
##halogen increments        
        self.entry_N_16.grid(row=1, column = 5, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_17.grid(row=2, column = 5, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_18.grid(row=3, column = 5, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_19.grid(row=4, column = 5, columnspan = 1, padx = 5, sticky = "sw")
##oxygen increments       
        self.entry_N_20.grid(row=1, column = 7, columnspan = 1, padx = 5, sticky = "sw")      
        self.entry_N_21.grid(row=2, column = 7, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_22.grid(row=3, column = 7, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_23.grid(row=4, column = 7, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_24.grid(row=5, column = 7, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_25.grid(row=6, column = 7, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_26.grid(row=7, column = 7, columnspan = 1, padx = 5, sticky = "sw")      
        self.entry_N_27.grid(row=8, column = 7, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_28.grid(row=9, column = 7, columnspan = 1, padx = 5, sticky = "sw")        
        self.entry_N_29.grid(row=10, column = 7, columnspan = 1, padx = 5, sticky = "sw")
##nitrogen increments       
        self.entry_N_30.grid(row=1, column = 9, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_31.grid(row=2, column = 9, columnspan = 1, padx = 5, sticky = "sw")      
        self.entry_N_32.grid(row=3, column = 9, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_33.grid(row=4, column = 9, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_34.grid(row=5, column = 9, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_35.grid(row=6, column = 9, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_36.grid(row=7, column = 9, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_37.grid(row=8, column = 9, columnspan = 1, padx = 5, sticky = "sw")        
        self.entry_N_38.grid(row=9, column = 9, columnspan = 1, padx = 5, sticky = "sw")
##sulfur increments       
        self.entry_N_39.grid(row=1, column = 11, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_40.grid(row=2, column = 11, columnspan = 1, padx = 5, sticky = "sw")
        self.entry_N_41.grid(row=3, column = 11, columnspan = 1, padx = 5, sticky = "sw")

##############################bottom frame _1 #################################
        
        self.bottom_frame_1 = ttk.Frame(self.master, padding = (30, 15))
        self.bottom_frame_1.pack()

        ttk.Button(self.bottom_frame_1, text = "Compute Physical Properties",
                   command = self.compute_phys_properties, style = "TButton").pack()
        ttk.Button(self.bottom_frame_1, text = "Reset to Default",
                   command = self.reset_to_default, style = "TButton").pack()
        
##############################bottom frame  ###################################
        self.bottom_frame = ttk.Frame(self.master, padding = (30, 15))
        self.bottom_frame.pack()

####Labels at bottom for printing out results###
        self.L1a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L1a.grid(row=0, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L2a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L2a.grid(row=0, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        self.L3a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L3a.grid(row=1, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L4a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L4a.grid(row=1, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        self.L5a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L5a.grid(row=2, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L6a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L6a.grid(row=2, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        self.L7a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L7a.grid(row=3, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L8a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L8a.grid(row=3, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        self.L9a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L9a.grid(row=4, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L10a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L10a.grid(row=4, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        self.L11a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L11a.grid(row=5, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L12a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L12a.grid(row=5, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        self.L13a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L13a.grid(row=6, column = 0, columnspan = 32, padx = 5, sticky = "sw")
        self.L14a = ttk.Label(self.bottom_frame, text = "", font = ('Arial', 12, 'bold'), foreground="blue")
        self.L14a.grid(row=6, column = 33, columnspan = 32, padx = 5, sticky = "sw")
        
    def compute_phys_properties(self):
       
        ##[[], [], ...[]] in total 41 nested list inside a list
        DB = [[     0.0141,	-0.0012,65,	23.58,	-5.10,	-76.45,	-43.96,	1.95E+1,	-8.08E-3,	1.53E-4,	-9.67E-8,	0.908,	2.373,	548.29,	-1.719],
                    [0.0189,	0.0000,	56,	22.88,	11.27,	-20.64,	8.42,	-9.09E-1,	9.50E-2,	-5.44E-5,	1.19E-8,	2.590,	2.226,	94.16,	-0.199],
                    [0.0164,	0.0020,	41,	21.74,	12.64,	29.89,	58.36,	-2.30E+1,	2.04E-1,	-2.65E-4,	1.20E-7,	0.749,	1.691,	-322.15,1.187],
                    [0.0067,	0.0043,	27,	18.25,	46.43,	82.23,	116.02,	-6.62E+1,	4.27E-1,	-6.41E-4,	3.01E-7,	-1.460,	0.636,	-573.56,2.307],
                    [0.0113,	-0.0028,56,	18.18,	-4.32,	-9.630,	3.77,	2.36E+1,	-3.81E-2,	1.72E-4,	-1.03E-7,	-0.473,	1.724,	495.01,	-1.539],
                    [0.0129,	-0.0006,46,	24.96,	8.73,	37.97,	48.53,	-8.00,	        1.05E-1,	-9.63E-5,	3.56E-8,	2.691,	2.205,	82.28,	-0.242],
                    [0.0117,	0.0011,	38,	24.14,	11.14,	83.99,	92.36,	-2.81E+1,	2.08E-1,	-3.06E-4,	1.46E-7,	3.063,	2.138,	"NA",	"NA"],
                    [0.0026,	0.0028,	36,	26.15,	17.78,	142.14,	136.70,	2.74E+1,	-5.57E-2,	1.01E-4,	-5.02E-8,	4.720,	2.661,	"NA",	"NA"],
                    [0.0027,	-0.0008,46,	9.20,	-11.18,	79.30,	77.71,	2.45E+1,	-2.71E-2,	1.11E-4,	-6.78E-8,	2.322,	1.155,	"NA",	"NA"],
                    [0.0020,	0.0016,	37,	27.38,	64.32,	115.51,	109.82,	7.87,	         2.01E-2,	-8.33E-6,	1.39E-9,	4.151,	3.302,	"NA",	"NA"],
                    [0.0100,	0.0025,	48,	27.15,	7.75,	-26.80,	-3.68,	-6.03,	         8.54E-2,	-8.00E-6,	-1.80E-8,	0.490,	2.398,	307.53,	-0.798],
                    [0.0122,	0.0004,	38,	21.78,	19.88,	8.67,	40.99,	-2.05E+1,	1.62E-1,	-1.60E-4,	6.24E-8,	3.243,	1.942,	-394.29,1.251],
                    [0.0042,	0.0061,	27,	21.32,	60.15,	79.72,	87.88,	-9.09E+1,	5.57E-1,	-9.00E-4,	4.69E-7,	-1.373,	0.644,	"NA",	"NA"],
                    [0.0082,	0.0011,	41,	26.73,	8.13,	2.09,	11.30,	-2.14,	        5.74E-2,	-1.64E-6,	-1.59E-8,	1.101,	2.544,	259.65,	-0.702],
                    [0.0143,	0.0008,	32,	31.01,	37.02,	46.43,	54.05,	-8.25,	        1.01E-1,	-1.42E-4,	6.78E-8,	2.394,	3.059,	-245.74,0.912],
                    [0.0111,	-0.0057,27,	-0.03,	-15.78,	-251.92,-247.19,2.65E+1,	-9.13E-2,	1.91E-4,	-1.03E-7,	1.398,	-0.670,	"NA",	"NA"],
                    [0.0105,	-0.0049,58,	38.13,	13.55,	-71.55,-64.31,	3.33E+1,	-9.63E-2,	1.87E-4,	-9.96E-8,	2.515,	4.532,	625.45,	-1.814],
                    [0.0133,	0.0057,	71,	66.86,	43.43,	-29.48,	-38.06,	2.86E+1,	-6.49E-2,	1.36E-4,	-7.45E-8,	3.603,	6.582,	738.91,	-2.038],
                    [0.0068,	-0.0034,97,	93.84,	41.69,	21.06,	5.74,	3.21E+1,	-6.41E-2,	1.26E-4,	-6.87E-8,	2.724,	9.520,	809.55,	-2.224],
                    [0.0741,	0.0112,	28,	92.88,	44.45,	-208.04,-189.20,2.57E+1,	-6.91E-2,	1.77E-4,	-9.88E-8,	2.406,	16.826,	2173.72,-5.057],
                    [0.0240,	0.0184,	-25,	76.34,	82.83,	-221.65,-197.37,-2.81,	         1.11E-1,	-1.16E-4,	4.94E-8,	4.490,	12.499,	3018.17,-7.314],
                    [0.0168,	0.0015,	18,	22.42,	22.23,	-132.22,-105.00,2.55E+1,	-6.32E-2,	1.11E-4,       -5.48E-8,	1.188,	2.410,	122.09,	-0.386],
                    [0.0098,	0.0048,	13,	31.22,	23.05,	-138.16,-98.22,	1.22E+1,	-1.26E-2,	6.03E-5,	-3.86E-8,	5.879,	4.682,	440.24,	-0.953],
                    [0.0380,	0.0031,	62,	76.75,	61.20,	-133.22,-120.50,6.45,	         6.70E-2,	-3.57E-5,	2.86E-9,	4.189,	8.972,	340.35,	-0.350],
                    [0.0284,	0.0028,	55,	94.97,	75.97,	-164.50,-126.27,3.04E+1,	-8.29E-2,	2.36E-4,       -1.31E-7,	"NA",	6.645,	"NA",	"NA"],
                    [0.0379,	0.0030,	82,	72.24,	36.90,	-162.03,-143.48,3.09E+1,	-3.36E-2,	1.60E-4,       -9.88E-8,	3.197,	9.093,	740.92,	-1.713],
                    [0.0791,	0.0077,	89,	169.09,	155.50,	-426.72,-387.87,2.41E+1,	4.27E-2,	8.04E-5,       -6.87E-8,	11.051,	19.537,	1317.23,-2.578],
                    [0.0481,	0.0005,	82,	81.10,	53.60,	-337.92,-301.95,2.45E+1,	4.02E-2,	4.02E-5,	-4.52E-8,	6.959,	9.633,	483.88,	-0.966],
                    [0.0143,	0.0101,	36,	-10.50,	2.08,	-247.61,-250.83,6.82,	        1.96E-2,	1.27E-5,	-1.78E-8,	3.624,	5.909,	675.24,	-1.340],
                    [0.0243,	0.0109,	38,	73.23,	66.89,	-2.02,	14.07,2.69E+1,	        -4.12E-2,	1.64E-4,        -9.76E-8,	3.515,	10.788,	"NA",	"NA"],
                    [0.0295,	0.0077,	35,	50.17,	52.66,	53.47,	89.39,-1.21,	        7.62E-2,	-4.86E-5,	1.05E-8,	5.009,	6.436,	"NA",	"NA"],
                    [0.0130,	0.0114,	29,	52.82,	101.51,	31.65,75.61,1.18E+1,	        -2.30E-2,	1.07E-4,	-6.28E-8,	7.490,	6.930,	"NA",	"NA"],
                    [0.0169,	0.0074,	9,	11.74,	48.84,	123.34,	163.16,-3.11E+1,	2.27E-1,	-3.20E-4,	1.46E-7,	4.703,	1.896,	"NA",	"NA"],
                    [0.0255,	-0.0099,"NA",	74.60,	"NA",	23.61,	"NA",     "NA",	         "NA",	         "NA",	          "NA", 	"NA",	3.335,	"NA",	"NA"],
                    [0.0085,	0.0076,	34,	57.55,	68.40,	55.52,	79.93,	8.83,	      -3.84E-3,	         4.35E-5,	-2.60E-8,	3.649,	6.528,	"NA",	"NA"],
                    ["NA",  	"NA",	"NA",	83.08,	68.91,	93.70,	119.66,	5.69,	       -4.12E-3,	1.28E-4,	-8.88E-8,	"NA",	12.169,	"NA",	"NA"],
                    [0.0496,	-0.0101,91,	125.66,	59.89,	88.43,	89.22,	3.65E+1,	-7.33E-2,	1.84E-4,	-1.03E-7,	2.414,	12.851,	"NA",	"NA"],
                    [0.0437,	0.0064,	91,	152.54,	127.24,	-66.57,	-16.83,	2.59E+1,	-3.74E-3,	1.29E-4,	-8.88E-8,	9.679,	16.738,	"NA",	"NA"],
                    [0.0031,	0.0084,	63,	63.56,	20.09,	-17.33,	-22.99,	3.53E+1,	-7.58E-2,	1.85E-4,	-1.03E-7,	2.360,	6.884,	"NA",	"NA"],
                    [0.0119,	0.0049,	54,	68.78,	34.40,	41.87,	33.12,	1.96E+1,	-5.61E-3,	4.02E-5,	-2.76E-8,	4.130,	6.817,	"NA",	"NA"],
                    [0.0019,	0.0051,	38,	52.10,	79.93,	39.10,	27.76,	1.67E+1,	4.81E-3,	2.77E-5,	-2.11E-8,	1.557,	5.984,	"NA",	"NA"]]

        #print (len(DB))

        entry_index_by_users = []
        entry_data_by_users = []
        for index, data in enumerate([self.N_0.get(), self.N_1.get(), self.N_2.get(), self.N_3.get(), self.N_4.get(),
self.N_5.get(), self.N_6.get(), self.N_7.get(), self.N_8.get(), self.N_9.get(), self.N_10.get(), self.N_11.get(), self.N_12.get(), self.N_13.get(), self.N_14.get(),
self.N_15.get(), self.N_16.get(), self.N_17.get(), self.N_18.get(), self.N_19.get(),
self.N_20.get(), self.N_21.get(), self.N_22.get(), self.N_23.get(), self.N_24.get(),
self.N_25.get(), self.N_26.get(), self.N_27.get(), self.N_28.get(), self.N_29.get(),
self.N_30.get(), self.N_31.get(), self.N_32.get(), self.N_33.get(), self.N_34.get(),
self.N_35.get(), self.N_36.get(), self.N_37.get(), self.N_38.get(), self.N_39.get(),
self.N_40.get()]):
            if float(data) != 0.:
                entry_index_by_users.append(index)
                entry_data_by_users.append(float(data))

        fiveteen_columns = [] ##length  = 15*len(entry_index_by_users)
        for index, data in zip(entry_index_by_users, entry_data_by_users):
            for i in range(15):
                if DB[index][i] == "NA":
                    temp = "NA"
                else:
                    temp = data*DB[index][i]
                fiveteen_columns.append(temp)

        Tc = []
        Pc = []
        Vc = []
        Tb = []
        Tm = []
        Hfor = []
        Gf = []
        Cpa = []
        Cpb = []
        Cpc = []
        Cpd = []
        Hfus = []
        Hvap = []
        Ya = []
        Yb =[]        
        fc = fiveteen_columns ## short hand
        for i in range(len(entry_index_by_users)):
            Tc.append(fc[i*15])
            Pc.append(fc[i*15 + 1])
            Vc.append(fc[i*15 + 2])
            Tb.append(fc[i*15 + 3])
            Tm.append(fc[i*15 + 4])
            Hfor.append(fc[i*15 + 5])
            Gf.append(fc[i*15 + 6])
            Cpa.append(fc[i*15 + 7])
            Cpb.append(fc[i*15 + 8])
            Cpc.append(fc[i*15 + 9])
            Cpd.append(fc[i*15 + 10])
            Hfus.append(fc[i*15 + 11])
            Hvap.append(fc[i*15 + 12])
            Ya.append(fc[i*15 + 13])
            Yb.append(fc[i*15 + 14])         

###normal boiling point
        if self.BoilingPoint.get()== "":                           
            try:
                self.L1a.configure(text = "Normal Boiling Point [K]: {0}".format(198.2 + sum(Tb)))            
            except:
                self.L1a.configure(text = "Not computable!")
        else:
            self.L1a.configure(text = "Normal Boiling Point [K]: {0}".format(float(self.BoilingPoint.get())))    
###melting point
        try:
            self.L2a.configure(text = "Melting Point [K]: {0}".format(122.5 + sum(Tm)))
        except:
            self.L2a.configure(text = "Not computable!")
###Critical Temperature
        if self.BoilingPoint.get()== "":  
            try:
                nom = sum(Tb) + 198.2
                denom = 0.584 + 0.965*sum(Tc) - sum(Tc)**2
                value = nom/denom
                self.L3a.configure(text = "Critical Temperature [K]: {0}".format(value))
            except:
                self.L3a.configure(text = "Not computable!", font = ('Arial', 12, 'bold'))
        else:
            try:
                nom = float(self.BoilingPoint.get())
                denom = 0.584 + 0.965*sum(Tc) - sum(Tc)**2
                value = nom/denom
                self.L3a.configure(text = "Critical Temperature [K]: {0}".format(value))
            except:
                self.L3a.configure(text = "Not computable!", font = ('Arial', 12, 'bold'))           
            
###Critical Pressure
        try:
            denom = (0.113 + 0.0032*float(self.NoA.get()) - sum(Pc))**2
            value = 1./denom
            self.L4a.configure(text = "Critical Pressure [bar]: {0}".format(value))
        except:
            self.L4a.configure(text = "Not computable!")
###Critical Volume
        try:
            self.L5a.configure(text = "Critical Volume [cm^3/mol]: {0}".format(17.5 + sum(Vc)))
        except:
            self.L5a.configure(text = "Not computable!")
###Enthalpy of formation, ideal gas at 298 K
        try:
            self.L6a.configure(text = "Heat of Formation (Ideal Gas, 298 K) [kJ/mol]: {0}".format(68.29 + sum(Hfor)))
        except:
            self.L6a.configure(text = "Not computable!")
####Gibbs energy off formation, ideal gas, unit fugacity, at 298 K
        try:
            self.L7a.configure(text = "Gibbs Energy of Formation (Ideal Gas, 298 K) [kJ/mol]: {0}".format(53.88 + sum(Gf)))
        except:
            self.L7a.configure(text = "Not computable!")
###Heat capacity, ideal gas
        try:
            term_1 = sum(Cpa) - 37.93
            term_2 = (sum(Cpb) + 0.210)*float(self._temperature.get())
            term_3 = (sum(Cpc) - 3.91*10**(-4))*float(self._temperature.get())**2
            term_4 = (sum(Cpd) + 2.06*10**(-7))*float(self._temperature.get())**3
            value = term_1 + term_2 + term_3 + term_4
            self.L8a.configure(text = "Heat Capcity (Ideal Gas) [J/(mol.K)]: {0}".format(value))
        except:
            self.L8a.configure(text = "Not computable!")
###Enthalpy of vaporization at Tb
        try:
            self.L9a.configure(text = "Heat of Vaporization at Normal Boiling Point [kJ/mol]: {0}".format(15.30 + sum(Hvap)))
        except:
            self.L9a.configure(text = "Not computable!")
###Enthalpy of fusion
        try:
            self.L10a.configure(text = "Heat of Fusion [kJ/mol]: {0}".format(-0.88 + sum(Hfus)))
        except:
            self.L10a.configure(text = "Not computable!")
###Liquid viscosity
        try:
            exponent = (sum(Ya) - 597.82)/float(self._temperature.get()) + sum(Yb) - 11.202
            value = float(self.MoleWeight.get())*math.exp(exponent)
            self.L11a.configure(text = "Liquid Dynamic Viscosity [Pa.s]: {0}".format(value))
        except:
            self.L11a.configure(text = "Not computable!")
###Log P
        try:
            value = 1.46 + 0.11*float(self.NoC.get()) - 0.11*float(self.NHET.get())
            self.L12a.configure(text = "Log P : {0}".format(value))
        except:
            self.L12a.configure(text = "Not computable!")
##General solubility equation 1&2
        if int(self.GSEradio.get()) == 0:
            try:
                logP = 1.46 + 0.11*float(self.NoC.get()) - 0.11*float(self.NHET.get())
                value_1 = 10**(0.8 - logP - 0.01*(sum(Tm)+122.5 - 273.15 - 25.))*1000.*float(self.MoleWeight.get())
                self.L13a.configure(text = "Aqueous Solubility [ug/ml] : {0}".format(value_1))
            except:
                self.L13a.configure(text = "Not computable!")
        elif int(self.GSEradio.get()) == 1:
            try:
                logP = 1.46 + 0.11*float(self.NoC.get()) - 0.11*float(self.NHET.get())
                value = 10**(0.5 - logP - 0.01*(sum(Tm)+122.5 - 273.15 - 25.)) *1000.*float(self.MoleWeight.get())
                self.L13a.configure(text = "Aqueous Solubility [ug/ml] : {0}".format(value))
            except:
                self.L13a.configure(text = "Not computable!")
###Amorphous solubility
        if int(self.GSEradio.get()) == 0:
            try:
                logP = 1.46 + 0.11*float(self.NoC.get()) - 0.11*float(self.NHET.get())
                value1 = 10**(0.8 - logP - 0.01*(sum(Tm)+122.5 - 273.15 - 25.)) *1000.*float(self.MoleWeight.get())
                nom = (sum(Hfus)-0.88)*(sum(Tm) + 122.5 - float(self._temperature.get()))*float(self._temperature.get())
                denom = (sum(Tm) + 122.5)**2
                RT = 2.479*float(self._temperature.get())/298.
                content = (nom/denom)/RT
                value2 = math.exp(content)
                value = value1*value2                
                self.L14a.configure(text = "Amorphous Solubility [ug/ml] : {0}".format(value))
            except:
                self.L14a.configure(text = "Not computable!")
        elif int(self.GSEradio.get()) == 1:
            try:
                logP = 1.46 + 0.11*float(self.NoC.get()) - 0.11*float(self.NHET.get())
                value1 = 10**(0.5 - logP - 0.01*(sum(Tm)+122.5 - 273.15 - 25.)) *1000.*float(self.MoleWeight.get())
                nom = (sum(Hfus)-0.88)*(sum(Tm) + 122.5 - float(self._temperature.get()))*float(self._temperature.get())
                denom = (sum(Tm) + 122.5)**2
                RT = 2.479*float(self._temperature.get())/298.
                content = (nom/denom)/RT
                value2 = math.exp(content)
                value = value1*value2                
                self.L14a.configure(text = "Amorphous Solubility [ug/ml] : {0}".format(value))
            except:
                self.L14a.configure(text = "Not computable!")
           
    def reset_to_default(self):
        ##set entry box to 0
        self.N_0.set(0)        
        self.N_1.set(0)
        self.N_2.set(0)
        self.N_3.set(0)
        self.N_4.set(0)
        self.N_5.set(0)
        self.N_6.set(0)
        self.N_7.set(0)
        self.N_8.set(0)
        self.N_9.set(0)
        self.N_10.set(0)
        self.N_11.set(0)
        self.N_12.set(0)
        self.N_13.set(0)
        self.N_14.set(0)
        self.N_15.set(0)
        self.N_16.set(0)
        self.N_17.set(0)
        self.N_18.set(0)
        self.N_19.set(0)
        self.N_20.set(0)
        self.N_21.set(0)
        self.N_22.set(0)
        self.N_23.set(0)
        self.N_24.set(0)
        self.N_25.set(0)
        self.N_26.set(0)
        self.N_27.set(0)
        self.N_28.set(0)
        self.N_29.set(0)
        self.N_30.set(0)
        self.N_31.set(0)
        self.N_32.set(0)
        self.N_33.set(0)
        self.N_34.set(0)
        self.N_35.set(0)
        self.N_36.set(0)
        self.N_37.set(0)
        self.N_38.set(0)
        self.N_39.set(0)
        self.N_40.set(0)
       ##set checkbutton to 0
        self.var_0.set(0)        
        self.var_1.set(0)
        self.var_2.set(0)
        self.var_3.set(0)
        self.var_4.set(0)
        self.var_5.set(0)
        self.var_6.set(0)
        self.var_7.set(0)
        self.var_8.set(0)
        self.var_9.set(0)
        self.var_10.set(0)
        self.var_11.set(0)
        self.var_12.set(0)
        self.var_13.set(0)
        self.var_14.set(0)
        self.var_15.set(0)
        self.var_16.set(0)
        self.var_17.set(0)
        self.var_18.set(0)
        self.var_19.set(0)
        self.var_20.set(0)
        self.var_21.set(0)
        self.var_22.set(0)
        self.var_23.set(0)
        self.var_24.set(0)
        self.var_25.set(0)
        self.var_26.set(0)
        self.var_27.set(0)
        self.var_28.set(0)
        self.var_29.set(0)
        self.var_30.set(0)
        self.var_31.set(0)
        self.var_32.set(0)
        self.var_33.set(0)
        self.var_34.set(0)
        self.var_35.set(0)
        self.var_36.set(0)
        self.var_37.set(0)
        self.var_38.set(0)
        self.var_39.set(0)
        self.var_40.set(0)
        
        ##set temperature, molecular weight and number of atoms to default value
        self._temperature.set(298)
        self.NoA.set(30)
        self.MoleWeight.set(100)
        self.NoC.set(15)
        self.NHET.set(1)
        self.GSEradio.set(0)
        self.BoilingPoint.set("")

        ##clear label
        self.L1a.configure(text = "")
        self.L2a.configure(text = "")
        self.L3a.configure(text = "")
        self.L4a.configure(text = "")
        self.L5a.configure(text = "")
        self.L6a.configure(text = "")
        self.L7a.configure(text = "")
        self.L8a.configure(text = "")
        self.L9a.configure(text = "")
        self.L10a.configure(text = "")
        self.L11a.configure(text = "")
        self.L12a.configure(text = "")
        self.L13a.configure(text = "")
        self.L14a.configure(text = "")

def main():            
    
    root = Tk()
    GUI = Hand_Pick(root)
    root.mainloop()
    
if __name__ == "__main__": main()
