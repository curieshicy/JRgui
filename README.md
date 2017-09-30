## A brief description of JRgui program:

By using the modern object-oriented programming language Python (e.g. tkinter and pandas modules) and a chemoinformatics open source library (RDKit), the classic Joback and Reid group contribution method was revisited and written into a graphical user interface program—JRgui. The underlying algorithm behind the program is explained, herein, with the user being able to operate the program in either a manual and automatic mode. In the manual mode, the users are required to determine the type and occurrence of functional groups in the compound of interest and manually enter into the program. In the automatic mode, both of these parameters can be detected automatically via user input of the compound SMILES string. An additional advantage of the automatic mode is that a large number of molecules can be processed simultaneously by parsing their individual SMILES strings into a text file which is read by the program. The resulting predicted physical properties along with approximately 200 molecular descriptors are saved in a spreadsheet file for subsequent analysis. It is hoped that the current work may facilitate the creation of other user friendly programs in the chemoinformatics community by using Python.

## The main interface of JRgui program:

![1n](https://user-images.githubusercontent.com/8492535/31049114-df926e6c-a5f1-11e7-9da8-ad9d0602e533.png)

## The manual mode in JRgui program:
![2n](https://user-images.githubusercontent.com/8492535/31049131-243170f4-a5f2-11e7-8f90-a7d97577ae96.png)

## The auto mode in JRgui program:
![3n](https://user-images.githubusercontent.com/8492535/31049115-df9e03c6-a5f1-11e7-92a8-33f2cf47dc90.png)

## Install and Use JRgui program (Support Windows, Linux, macOS, 64-bit systems): 
The recommended way to install JRgui is via <b>conda install</b>. The initial step is to install Anaconda python distribution (https://www.anaconda.com/download/) for Windows, Linux or macOS. Choose 64-bit and Python 3.6 version for download and install. After download and install it, start a terminal (in Windows use <b>Anaconda Prompt</b> not default terminal), type <b>conda --version</b> to check out if conda has been successfully installed. 

Once conda has been installed, (in the terminal) type <b>conda create -c curieshicy -n my-jrgui-env jrgui</b>. Conda will automatically find dependency packages and install them all. This one-line command first adds my conda channel <b>curieshicy</b> and then creates a virtural environment named <b>my-jrgui-env</b> where all dependency Python packages will be installed. The usage of a virtural environment has the advantage of avoiding potential conflicts of different versioned Python installed at default system path. The specific environment created will be only used for JRgui program. 

To use JRgui program, the users first need to activate the virtural environment (in Windows type <b>activate my-jrgui-env</b>; in Linux and MacOS type <b>source activate my-jrgui-env</b>. To quit virtural environment replace <b>activate</b> with <b>deactivate</b>), and type <b>jrgui</b> to invoke the GUI. 

For Windows users (7, 8 and 10, 64-bit), the standlone executalbe files are also avaliable. The users only need to download the correct file for their operation system. To use it simple double-click it to invoke the GUI. These executables are created by using Pyinstaller.

## Citation:

If you use this program and like it, please consider citing: <i>Chenyang Shi and Thomas B. Borchardt, "JRgui: A python program of Joback and Reid method", submitted</i>. 
