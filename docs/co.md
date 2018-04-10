# How to run your code on the free GPU google colab server

You need a google account to use google colab [https://colab.research.google.com](https://colab.research.google.com). In google colab you can upload, edit and run ipython notebooks. Tensorflow and keras along with the most important packages are already installed and additional packages can be added by system calls from the ipython notebook (!pip install ...). It is possible to upload and download data or checkpoints with model weights and we have prepared an [example notebook](https://drive.google.com/file/d/1ywf7RP-LYpmJZk7xSUMpCXImwajYoXjA/view?usp=sharing). You can directly open the notebook with the google colab app, activate the playground and check out how to work on google colab - for running the provided example you need to upload the [iris data](https://www.dropbox.com/s/zz35u19ihy63x5u/iris.csv?dl=1) which you can also find in the data folder of our github repository.

### Starting notebooks from github in colab 

If you want to open a notebook straight from github into google colab, you can use the following url:


```
 'https://colab.research.google.com/github/' + repository + 'blob/master/' + file_in_repository
```

so if you want to open the notebook `00...` from our course do:

 [https://colab.research.google.com/github/tensorchiefs/dl_course_2018/blob/master/notebooks/00_Checking_Correct_Installation.ipynb](https://colab.research.google.com/github/tensorchiefs/dl_course_2018/blob/master/notebooks/00_Checking_Correct_Installation.ipynb)

