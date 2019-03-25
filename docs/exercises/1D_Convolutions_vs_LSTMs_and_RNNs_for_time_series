---
layout: default
mathjax: true
title: Deep Learning Course 
---
## 1D Convolutions vs LSTMs and RNNs for time series
 
In this notebook we will use diffrent network architectures to predict the next steps for a time series.   
We compare 1D convolutional networks with and without didilation rate and LSTMs.   
We predict the time series for longer times than we trained them on and compare the resuts of the diffrent architectures.   
The goal is to capture the long term dependencies of the time series.  
Our data generating process of the time series is a fast sine wave multiplied with a slower sine wave plus a bit of random noise


a) Open the notebook [LSTM_vs_1DConv](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/12_LSTM_vs_1DConv.ipynb)  
Look at the data generating process and train the first "1D Convolution without dilation rate" model and look at the predictions for the next
10 and 80 time steps. What to you observe, did the model learn the data generating process?

b) Complete the code in the "1D Convolution with dilation rate" part. Use the same architecture as in the 1D Convolution model from above.  
Just add the argument dilation_rate in the Convolution1D-Layer, start with the dilation_rate 1 and then multiply it by 2 (1,2,4,8).  
Look at the predictions for the next 10 and 80 time steps. What to you observe, now? Did the model learn the data generating process?

c) Now Lets use a LSTM for the same process. How good are the predictions for the 10 and 80 time steps?
Did the model learn the data generating process? 
Compare the Results in the "1D Convolution with dilation rate vs LSTM for very long prediction" part, which model captures the process better.

d) Now Lets use a replace the LSTM cell with a RNN cell, in keras SimpleRNN. Use the same size of units and the same architectures.
Do we need a complex LSTM cell or is the RNN cell good enough for this process?
