---
layout: default
mathjax: true
title: Deep Learning Course 
---
## Convolutional Neural Networks for image data

We want to investigate, if a CNN outperforms a fc NN on image data.  

First we recall the design of the fc NN which performed so far best on MNIST when only keeping 2400 examples in the 
training data set (see below). With this NN we have reached ~91% accuracy on the validation data set. 
[fcn_MNIST_keras](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/06_fcn_MNIST_keras_solution.ipynb)
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 500)               392500    
_________________________________________________________________
batch_normalization_1 (Batch (None, 500)               2000      
_________________________________________________________________
dropout_1 (Dropout)          (None, 500)               0         
_________________________________________________________________
activation_1 (Activation)    (None, 500)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 50)                25050     
_________________________________________________________________
batch_normalization_2 (Batch (None, 50)                200       
_________________________________________________________________
dropout_2 (Dropout)          (None, 50)                0         
_________________________________________________________________
activation_2 (Activation)    (None, 50)                0         
_________________________________________________________________
dense_3 (Dense)              (None, 10)                510       
=================================================================
Total params: 420,260.0
Trainable params: 419,160.0
Non-trainable params: 1,100.0
_________________________________________________________________
```

a) Where do we spend most learnable parameter? Can you explain the "Param #" of the dense_1 layer?  
Remark: dense layer is the same as fully connected layer.

b) Now we want to use our first CNN with only 1 convolutional and 1 dense layer:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 28, 28, 32)        320       
_________________________________________________________________
activation_1 (Activation)    (None, 28, 28, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 25088)             0         
_________________________________________________________________
dense_1 (Dense)              (None, 10)                250890    
_________________________________________________________________
activation_2 (Activation)    (None, 10)                0         
=================================================================
Total params: 251,210
Trainable params: 251,210
Non-trainable params: 0
_________________________________________________________________
```

In which layer do we need to learn most parameter/weights?

Do you expect with this cnn1 more or less overfitting then in the fc NN above? Why?

Please open the ipython-Notebook [cnn1_mnist](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/07_cnn1_mnist.ipynb) and 
try to understand the code and run the code.

Train the model without first standardizing the data which would be done in code cell 7 (cell is a comment here).  
What is the accuracy on the validation set, now?  
Can you explain, what happened?

Now train the model with standardizing the data by running the rest of the cells.
How good is the accuracy on the validation and test set now?  
Do you observe overfitting?  
Describe how you check for overfitting and/or sketch the corresponding graph.


c) Lets use more Convolutional Layers and also Dropout and Batchnorm.  
Please open the ipython-Notebook [cnn2_mnist](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/08_cnn2_mnist.ipynb).   
Look for the position in the code which is marked by "# here is your code coming:" and add the missing layers - the missing layers are marked  below.  
How is the performance of cnn2?
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 28, 28, 8)         80        
_________________________________________________________________
batch_normalization_1 (Batch (None, 28, 28, 8)         32        
_________________________________________________________________
activation_1 (Activation)    (None, 28, 28, 8)         0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 28, 28, 8)         584       
_________________________________________________________________
batch_normalization_2 (Batch (None, 28, 28, 8)         32        
_________________________________________________________________
activation_2 (Activation)    (None, 28, 28, 8)         0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 14, 14, 8)         0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 14, 14, 16)        1168      
_________________________________________________________________
batch_normalization_3 (Batch (None, 14, 14, 16)        64        
_________________________________________________________________
activation_3 (Activation)    (None, 14, 14, 16)        0         
_________________________________________________________________ 
--------------------START OF THE MISSING LAYERS------------------

conv2d_4 (Conv2D)            (None, 14, 14, 16)        2320      
_________________________________________________________________
batch_normalization_4 (Batch (None, 14, 14, 16)        64        
_________________________________________________________________
activation_4 (Activation)    (None, 14, 14, 16)        0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 7, 7, 16)          0         
_________________________________________________________________

--------------------END OF THE MISSING LAYERS--------------------
flatten_1 (Flatten)          (None, 784)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 40)                31400     
_________________________________________________________________
batch_normalization_5 (Batch (None, 40)                160       
_________________________________________________________________
dropout_1 (Dropout)          (None, 40)                0         
_________________________________________________________________
activation_5 (Activation)    (None, 40)                0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                410       
_________________________________________________________________
activation_6 (Activation)    (None, 10)                0         
=================================================================
Total params: 36,314
Trainable params: 36,138
Non-trainable params: 176
_________________________________________________________________
```
