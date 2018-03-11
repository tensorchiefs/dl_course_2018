---
layout: default
mathjax: true
title: Deep Learning Course 
---
## 8 faces competition

In this competition we work with the 8 faces dataset. this dataset has 350 images of 8 celebrities.  
To get an overview of the data open the notebook [8 faces overview](https://www.dropbox.com/sh/oek6lcshf9ws8o4/AAB5hSpN328raDkbdYHH_YsQa?dl=0&preview=8_faces_dataoverview.html) and look at the celebrities and the images.  
The data is a random sample of 8 persons of the OXFORD VGG Face dataset (over 2600 Persons),  
for more information look here: [http://www.robots.ox.ac.uk/~vgg/data/vgg_face/](http://www.robots.ox.ac.uk/~vgg/data/vgg_face/)  

a) Have a look at the [8_faces_fc](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/09_8_faces_fc.ipynb) notebook       
In this notebook we traind a fully connected neural network on the dataset. The accuracy of this network on the validation data is ~60%.
You can also see how to save and reload a trained model in keras, you will have to do that for the next task.

## 8 faces your own model

b)  Now it's your turn!  
Design a network that outperforms our baseline fc model.  
You will get the test data next week and the team with the best accuracy on the test data will get a price.  

Hint 1: Is it a good idea to use a fully connected neural network on this dataset?  

Hint 2 : The training of more complex networks could take some time because we compute only on cpu.  
(up to 1h)
