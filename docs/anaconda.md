## Technical Prerequistes

The course is taught in python using using jupyter notebooks. The deep learning libraries are tensorflow and keras.  

### Installation instructions
There two ways, how to run these notebooks, a provided docker container or via anaconda. 


#### Anaconda Installation

* [Download](https://www.anaconda.com/download/) the Anaconda Version for python 3.6 required for you operation system.  For Windows use the "Just me" option (system-wide will only work, if you make sure that all users have write access to the install directory).

* Create a virtual environment for the course
	```
	conda create -n dl_course anaconda
	```
	Windows user can use the Anaconda Navigator GUI to create an new environment. Directly typing comands can be done in the Anaconda Prompt window which can be opened via the Start Menue button. Within the Anaconda Prompt one can use *dir* and *cd* to find and change between different environments.

* Activate the environment
	```
	source activate dl_course
	#or
	activate dl_course
	```
	

* Install the following required packages
	```
	conda install tensorflow=1.12.0
	conda install keras=2.2.4 
	conda install -c conda-forge ipywidgets
	```


#### Starting the notebook

Once you installed anaconda you can start the notebooks via (you might need to activate the environment) 

```
jupyter notebook
```

#### Checking the installation
Please make sure that the following notebook is working
<a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/00_Checking_Correct_Installation.ipynb'>00_Checking_Correct_Installation.ipynb</a>







