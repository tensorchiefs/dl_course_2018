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

* Activate the environment
	```
		source activate dl_course
	```

* Install the following required packages
	```
		conda install tensorflow=1.1.0
		conda install keras 
	```


#### Starting the notebook

Once you installed anaconda you can start the notebooks via (you might need to activate the environment) via 

```
  jupyter notebook
```







