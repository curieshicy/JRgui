## A brief description of JRgui program:

By using the modern object-oriented programming language Python (e.g. tkinter and pandas modules) and a chemoinformatics open source library (RDKit), the classic Joback and Reid group contribution method was revisited and written into a graphical user interface program—JRgui. The underlying algorithm behind the program is explained, herein, with the users being able to operate the program in either a manual and automatic mode.  In the manual mode, the users are required to determine the type and occurrence of functional groups in the compound of interest and manually enter into the program. In the automatic mode, both of these parameters can be detected automatically via user input of the compound SMILES string.  An additional advantage of the automatic mode is that a large number of molecules can be processed simultaneously by parsing their individual SMILES strings into a text file which is read by the program. The resulting predicted physical properties along with approximately 200 molecular descriptors are saved in a spreadsheet file for subsequent analysis. The program is freely available from https://github.com/curieshicy/JRgui for Windows, Linux and macOS 64-bit operating systems. It is hoped that the current work may facilitate the creation of other user friendly programs in the chemoinformatics community by using Python. 

## The main interface of JRgui program:

![1n](https://user-images.githubusercontent.com/8492535/31049114-df926e6c-a5f1-11e7-9da8-ad9d0602e533.png)

## The manual mode in JRgui program:
![2n](https://user-images.githubusercontent.com/8492535/31049131-243170f4-a5f2-11e7-8f90-a7d97577ae96.png)

## The auto mode in JRgui program:
![3n](https://user-images.githubusercontent.com/8492535/31049115-df9e03c6-a5f1-11e7-92a8-33f2cf47dc90.png)

## Install and Use JRgui program (Support Windows, Linux and macOS 64-bit systems): 
### Recommended Installation Method--Using <b>Conda install</b>

The recommended way to install JRgui is via <b>conda install</b>. The initial step is to install Anaconda python distribution (https://www.anaconda.com/download/) for Windows, Linux and macOS OS. Choose 64-bit and Python 3.6 version for download and install. After download and install it, start a terminal (in Windows use <b>Anaconda Prompt</b> NOT default terminal), type <b>conda --version</b> to check if conda has been successfully installed. 

Once conda has been installed, (in the terminal) type the following two commands

<b>conda config --add channels rdkit</b> 

<b>conda create -c curieshicy -n my-jrgui-env jrgui</b> 

The first command adds the channel of a dependency package--rdkit (One may use <b>conda config --get channels</b> to check channels that have been added). The second one-line command first adds my conda channel <b>curieshicy</b> and then creates a virtural environment named <b>my-jrgui-env</b> where all dependency Python packages will be installed. The usage of a virtural environment has the advantage of avoiding potential conflicts of different versioned Python installed at default system path. The specific environment created will be only used for JRgui program. After executing these two line-commands Conda will automatically find dependency packages and install them all. 

To use JRgui program, the users first need to activate the virtural environment (in Windows type <b>activate my-jrgui-env</b>; in Linux type <b>source activate my-jrgui-env</b>. To quit virtural environment replace <b>activate</b> with <b>deactivate</b>), and type <b>jrgui</b> to invoke the GUI. 

<b>Note</b> For macOS system, as of 10/27/2017, please make sure to install your conda with a version number 4.3.25, which can be done by typing 

<b>conda install conda=4.3.25</b>

Otherwise when loading RDKit, it will show error messages such as "Fatal Python error: PyThreadState_Get: no current thread" or "Segmentation fault: 11". Please see the post by the author of RDKit, Dr. Greg Landrum on this bug/issue (https://www.mail-archive.com/rdkit-discuss@lists.sourceforge.net/msg07325.html).

The installation and test of JRgui program has been performed on Windows 7, 8.1, 10, Linux Ubuntu 14.04.5 and macOS 10.10.3 (all 64-bit OS). For your reference, the corresponding screenshots are accessible at https://github.com/curieshicy/JRgui/tree/master/Installation_and_Test. 

### What if Conda install fails?
(It is not supposed to but...) For some reason, if the conda install method fails, the users can always download the source codes and manually invoke the GUI interface. To do this, for example, on a Windows platform, first install rdkit package (make sure Anaconda has been installed) by typing in a Anaconda Prompt terminal:

<b>conda create -c rdkit -n my-rdkit-env rdkit</b>

Download the source codes (i.e. molecule.gif and jrgui.py to e.g. C:\Users\username\Desktop\Source_Codes), in the Anaconda Prompt terminal, activate rdkit environment by typing 

<b>activate my-rdkit-env</b>

navigate to <b>Source_Codes</b> folder, and type 

<b>python jrgui.py</b> 

to invoke the GUI interface.

### Questions and suggestions

Questions and suggestions are welcome. You may contact me at cs3000@columbia.edu. Thanks for considering using JRgui.

## Citation:

If you use this program and like it, please consider citing: 

Chenyang Shi and Thomas B. Borchardt, "JRgui: A python program of Joback and Reid method",<i> ACS Omega</i>, <b>2(12)</b>, (2017), 8682–8688 (<a href = "http://pubs.acs.org/doi/full/10.1021/acsomega.7b01464">Link</a>). 

## Acknowledgement:

I thank helps from Jason Biggs when developing and testing SMARTS codes for functional groups used in Joback and Reid method. 
