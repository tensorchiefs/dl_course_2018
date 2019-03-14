---
layout: default
mathjax: true
title: Deep Learning Course 
---
## 8 faces fine tuning
 
In this excercise we work with the 8 faces dataset. We want to improve the performance by using a  
pretrained vgg16 network. We predict the features on the fc1 layer with the already learned weights on imagenet 
and then train a small fully connected network for our own labels. The feature extraction was done in this notebook 
[vgg16_feature_extraction_8_faces](https://github.com/tensorchiefs/dl_course/blob/master/notebooks/12_vgg_feature_extraction_without_relu_8_faces.ipynb)

a) What do you expect, will it increase our performance? Why? What's the idea behind this so called fine tuning or transfer learning?


b) Open the notebook [8 faces fine tuning](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/11_8_faces_fine_tuning.ipynb) and build this network and train it.  
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 400)               1638800   
_________________________________________________________________
batch_normalization_1 (Batch (None, 400)               1600      
_________________________________________________________________
activation_1 (Activation)    (None, 400)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 400)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 400)               160400    
_________________________________________________________________
batch_normalization_2 (Batch (None, 400)               1600      
_________________________________________________________________
activation_2 (Activation)    (None, 400)               0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 400)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 200)               80200     
_________________________________________________________________
batch_normalization_3 (Batch (None, 200)               800       
_________________________________________________________________
activation_3 (Activation)    (None, 200)               0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 200)               0         
_________________________________________________________________
dense_4 (Dense)              (None, 8)                 1608      
_________________________________________________________________
activation_4 (Activation)    (None, 8)                 0         
=================================================================
Total params: 1,885,008
Trainable params: 1,883,008
Non-trainable params: 2,000
_________________________________________________________________

```

b) Complete the code to get the probabilities for each image of the test set  
and take a look at the confusion matrix and the accuracy on the test data.  
Compare it with the FCN and CNN solution.
