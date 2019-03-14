---
layout: default
mathjax: true
title: Deep Learning Course 
---
## 8 faces FCN

In this exercise we work with the 8 faces dataset. this dataset has 350 images of 8 celebrities.  
To get an overview of the data open the notebook [8 faces overview](https://www.dropbox.com/sh/oek6lcshf9ws8o4/AAB5hSpN328raDkbdYHH_YsQa?dl=0&preview=8_faces_dataoverview.html) and look at the images.  
The data is a random sample of 8 persons of the OXFORD VGG Face dataset (over 2600 Persons),  
for more information look here: [http://www.robots.ox.ac.uk/~vgg/data/vgg_face/](http://www.robots.ox.ac.uk/~vgg/data/vgg_face/)  

a) Have a look at the [8_faces_fc](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/09_8_faces_fc.ipynb) notebook and try to understand it.  
In this notebook we traind a fully connected neural network on the dataset. The accuracy of this network on the validation data is ~60%.
You can also see how to save and reload a trained model in keras, you will have to do that for the next task.

## 8 faces your own model CNN

b)  Now it's your turn!  
Design a network that outperforms this baseline fc model.
You can use the test data the check how good your model performs on new unseen data.


Hint 1: Is it a good idea to use a fully connected neural network on this dataset?  
Hint 2 : The training of more complex networks could take some time because we compute only on cpu. (up to 1h)  
Hint 3 : Look at the possible solution to get some ideas [8_faces_cnn](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/10_8_faces_cnn.ipynb)
