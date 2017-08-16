## A brief description of JRgui program:

By using the modern object-oriented programming language Python (e.g. tkinter and pandas modules) and a chemoinformatics open source library (RDKit), the classic Joback and Reid group contribution method was revisited and written into a graphical user interface program—JRgui. The underlying algorithm behind the program is explained, herein, with the user being able to operate the program in either a manual and automatic mode. In the manual mode, the users are required to determine the type and occurrence of functional groups in the compound of interest and manually enter into the program. In the automatic mode, both of these parameters can be detected automatically via user input of the compound SMILES string. An additional advantage of the automatic mode is that a large number of molecules can be processed simultaneously by parsing their individual SMILES strings into a text file which is read by the program. The resulting predicted physical properties along with approximately 200 molecular descriptors are saved in a spreadsheet file for subsequent analysis. It is hoped that the current work may facilitate the creation of other user friendly programs in the chemoinformatics community by using Python.

## The main interface of JRgui program:

![jrgui_main_window](https://user-images.githubusercontent.com/8492535/29347443-51c28124-8212-11e7-9ea9-cda3ac0d5d96.png)

## There are two options to use JRgui program: 

(1) Download/Check out original Python files (Main.py, Joback_Hand_Pick.py, Joback_Smiles.py and molecule.gif) and put them in one folder. After installing necessary Python packages (RDkit, tkinter, pandas, default Python, all versions >3), use terminal to navigate into the folder, type Main.py to invoke the program. 

(2) If you do not wish to install any Python packages, you may choose to download a single standalone executable file (JRgui_windows.exe for Windows and JRgui_Linux for Linux operation system). After download the executable file, to start the program, either double click it or use a terminal. 

If you like the program please consider cite our paper "JRgui: A Python program of Joback and Reid Method", under review at ACS Omega.
