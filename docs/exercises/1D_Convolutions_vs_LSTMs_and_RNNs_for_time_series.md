---
layout: default
mathjax: true
title: Deep Learning Course 
---
## 1D Convolutions vs LSTMs and RNNs for time series
 
In this notebook we will use different network architectures to predict the next steps for a time series.   
We compare 1D convolutional networks with and without dilation rate, SimpleRNNs and LSTMs.  
We predict the time series for longer times than we trained them on and compare the results of the different architectures.   
The goal is to capture the long term dependencies of the time series.  
Our data generating process of the time series is a fast sine wave multiplied with a slower sine wave plus a bit of random noise


a) Open the notebook [LSTM_vs_1DConv](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/12_LSTM_vs_1DConv.ipynb)  
Look at the data generating process and train the first "1D Convolution without dilation rate" model and look at the predictions for the next
10 and 80 time steps.  
What to you observe, did the model learn the data generating process?  
How big is the receptive field in the last convolutional layer?


b) Complete the code in the "1D Convolution with dilation rate" part. Use the same architecture as in the 1D Convolution model from above.  
Just add the argument dilation_rate in the Convolution1D-Layer, start with the dilation_rate 1 and then multiply it by 2 (1,2,4,8).  
Look at the predictions for the next 10 and 80 time steps.  
What to you observe, now? Did the model learn the data generating process?  
How big is the receptive field in the last convolutional layer, now?


c) Now, Let's use a RNN for the same process. How good are the predictions for the 10 and 80 time steps?  
What does the argument return_sequences mean?   
How many weights do we need if we use a hidden state size of 12, check your calculations with the model.summary().    
Did the model learn the data generating process?  


d) Let's replace the RNN cell with a more complex LSTM cell, in keras LSTM.  
Use the same size of units and the same architecture.  
How many weights do we need now?

e) Compare the 4 models for very long predictions (800 timesteps).
What do you observe?  
What could we do to improve the RNN and the Conv1D with dilation_rate?
