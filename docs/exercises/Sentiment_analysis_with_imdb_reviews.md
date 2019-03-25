---
layout: default
mathjax: true
title: Deep Learning Course 
---
## Sentiment analysis with imdb reviews
 
In this notebook we work with the IMDb dataset, it is a binary sentiment analysis dataset consisting of 
50,000 reviews from the Internet Movie Database (IMDb) labeled as positive (1) or negative (0). 
The dataset contains an even number of positive and negative reviews. Only highly polarizing reviews are considered.
A negative review has a score ≤ 4 out of 10, and a positive review has a score ≥ 7 out of 10. 
We will apply a very simple preprocessing to the textreviews and then train a baseline classifier:  
A randomforest trained on bag of words features.  
We will compare the results of this baseline classifier with a neural network classifier, where we learn a dense 
word-embedding for each word and then classify it to either positive (1) or negative (0). 
Finally, we will use an inception-like architecture with 1D convolutions and globalpooling and see if we can improve the performace. 
You can test the trained network on new reviews from the internet or by writting your own review for a movie you like or don't like.

a) Open the notebook [Sentiment analysis with imdb reviews](https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/13_sentiment_analysis_with_imdb_reviews.ipynb)  
Read some of the reviews in cell 5 and try to label them into posivie or negative. Is this an easy task?  
Run the rest of the code to train a RF on the bag of words featrues and try to understand it.


b) Complete the code to build the architecture below (use a dropout rate of 0.5).  
Where do we need the most # of Parameters?   
What is the input and output of the Embedding layer?  
What is the global average pooling layer doing?
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_1 (Embedding)      (None, None, 30)          1868910   
_________________________________________________________________
global_average_pooling1d_1 ( (None, 30)                0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 30)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 20)                620       
_________________________________________________________________
dropout_2 (Dropout)          (None, 20)                0         
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 21        
=================================================================
Total params: 1,869,551
Trainable params: 1,869,551
Non-trainable params: 0
_________________________________________________________________

```
