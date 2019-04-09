---
layout: default
title: Deep Learning Course 2019
site.description: The 2019 Version of the DL Course
---
# Deep Learning (CAS machine intelligence, 2019) 

This course in deep learning focuses on practical aspects of deep learning. We therefore provide jupyter notebooks ([complete list of notebooks](list_of_notebooks.md) used in the course).

For doing the hands-on part on your own computer you can either install anaconda ([details and installation instruction](anaconda.md)) or use the provided a docker container ([details and installation instruction](docker.md)).

You can also execute the notebooks for the hands-on part on the cloud using binder 
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/tensorchiefs/dl_course_2018/master?filepath=notebooks) or open them in [colab](list_of_notebooks.md). 

To easily follow the course please make sure that you are familiar with the some [basic math and python skills](prerequistites.md). 

## Info for the projects
You can join together in small groups and choose a topic for your DL project. You should prepare a poster and a spotlight talk (5 minutes) which you will present on the last course day. To get some hints how to create a good poster you can check out the links that are provided in <a href="https://www.dropbox.com/s/u1f6mqk4pc3uhxe/poster-guidelines.pdf?dl=1">poster_guidelines.pdf</a> 

If you need free GPU resources, we might want to follow the [instructions how to use google colab](co.md). Help for preparing a hdf5 file from your images you can be found in the <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/data_prep.ipynb"> example Notebook.</a> 

Examples for projects from the DL course 2018 and 2019 can be found [here](projects.md).

## Other resources
We took inspiration (and sometimes slides / figures) from the following resources.

* Deep Learning Book (DL-Book) [http://www.deeplearningbook.org/](http://www.deeplearningbook.org/). This is a quite comprehensive book which goes far beyond the scope of this course.

* Convolutional Neural Networks for Visual Recognition [http://cs231n.stanford.edu/](http://cs231n.stanford.edu/), has additional material and [youtube videos of the lectures](https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC). While the focus is on computer vision, it also treats other topics such as optimization, backpropagation and RNNs. Lecture notes can be found at [http://cs231n.github.io/](http://cs231n.github.io/).

* More TensorFlow examples can be found at [dl_tutorial](https://github.com/oduerr/dl_tutorial/tree/master/tensorflow/) 

* Another applied course in DL: [TensorFlow and Deep Learning without a PhD](https://cloud.google.com/blog/big-data/2017/01/learn-tensorflow-and-deep-learning-without-a-phd)


## Dates 
The course is split in 8 sessions, each 4 lectures long. 
<table  class="zebra" width="width:100%">
  <tr>
      <th style="text-align: left;" width="%55">Day</th>
      <th style="text-align: left;" width="%55">Date</th>
      <th style="text-align: left;" width="%55">Time</th>
  </tr>
   <tr>
    <td>1</td>
    <td>Tue Feb 19</td>
    <td>13:30-17:00</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Tue Feb 26</td>
    <td>13:30-17:00</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Tue March 05</td>
    <td>13:30-17:00</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Tue March 12</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Tue March 19</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Tue March 26</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Tue April 02</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Tue April 09</td>
    <td>09:00-12:30</td>
  </tr>
 
</table>
<p>&nbsp;</p> <!-- leerer absatz -->

  
## Syllabus (might change during course)

<!--  
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Note on table no empty lines / Bitte keine Leerzeilen 
Otherwise the rendering is brolen
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-->
<table  class="zebra" width="width:100%">
  <tr>
      <th style="text-align: left;" width="%5">Day</th>
      <th style="text-align: left;" width="%55">Topic and slides</th>
      <th style="text-align: left;" width="%20">Additional Material</th>
      <th style="text-align: left;" width="%20">Exercises and homework</th>
  </tr>
    <!--  ------------------------------------- -->
    <!--  Woche 1 -->
    <!--  ------------------------------------- -->
    <tr>
    <td style="text-align: left;" valign="top">1</td>  
  	<td style="text-align: left;" valign="top"> 
        <b>Deep learning basics</b> <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/slides/DL2018-day1.pdf"> slides_day1</a>
      		<ul>
      			<li>Overview of deep learning</li>
      			<li>Computational graphs, feeding and fetching</li>
      			<li>Loss function (RMS)</li>
      			<li>Gradient descent and generalizations</li>
      			<li>Example: linear regression</li>
      		</ul>
    </td>
    <!--  Additional Material -->
    <td style="text-align: left;" valign="top"> 
    	<ul>
        <li> <a href='http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html'>Nature review article</a></li>
        <li> DL-book chapter 6</li>
        <li><a href="https://www.tensorflow.org/get_started/get_started">TensorFlow Intro</a></li>
	<li><a href="https://www.youtube.com/watch?v=l6K-MFgIEjc">Intro Lecture on TensorFlow form Stanford CS224d</a></li>
       </ul>
   	</td>    
    <!--  Exercises and Homework -->
    <td style="text-align: left;" valign="top">
    	<ul>
    		<li>
        		01 Matrix Multiplication 
            <a href="exercises/01_tf_matrix_mult"> Exercises</a> | 
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/01_MatrixMultiplication.ipynb'> Notebook</a> | 
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/01_MatrixMultiplication_solution.ipynb'> Solution</a> 
        </li>
    		<li>
        		02 Linreg (with_slider) 
            <a href="exercises/02_linreg_with_slider"> Exercises</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/02_Linreg_with_slider.ipynb'> Notebook</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/02_Linreg_with_slider_solution.ipynb'> Solution</a> 
        </li>
        <!-- 
        <li>
              03 Homework: Frozen Graph (Artstyle Transfer)
              <a href="exercises/03_Loading_Frozen_Graph"> Exercises</a> |
              <a href='https://github.com/tensorchiefs/dl_course/blob/master/notebooks/03_Loading_Frozen_Graph_solution.ipynb'> Solution Exercise</a> 
        </li>
    		<li>
    			 Homework: Mandelbrot <a href='https://github.com/oduerr/dl_tutorial/blob/master/tensorflow/simple_ops/Mandelbrot.ipynb'> Notebook</a> 
    		</li> 
        < -->
      </ul>
    </td>   
  </tr>
    <!--  ------------------------------------- -->
    <!--  Woche 2 -->
    <!--  ------------------------------------- -->
    <tr>
    <td style="text-align: left;" valign="top">2</td>  
    <td style="text-align: left;" valign="top"> 
       <b>Gradient Descent and loss functions for classification</b>  <a href="http://www-home.htwg-konstanz.de/~oduerr/docs/lecture02.pdf"> slides_day2</a>
          <ul>
            <li>Gradient Descent</li>
            <li>Logistic regression</li>
            <li>Multinomial Logistic Regression</li>
          </ul>
    </td>
    <!--  Additional Material -->
    <td style="text-align: left;" valign="top"> 
      <ul>
        <li> DL-book chapter 6</li>
        <li> DL-book chapter 3</li>
        <li> <a href="https://rdipietro.github.io/friendly-intro-to-cross-entropy-loss">Cross Entropy Loss </a></li>
       </ul>
    </td>    
    <!--  Exercises and Homework -->
    <td style="text-align: left;" valign="top">
      <ul>
          <li>
            <a href='exercises/03a_exercises_tf_playgound_day2'> log. reg. in TF-playground</a> 
          </li>
    		<li>
        		03 Logistic Regression (Challenger)
            <a href="exercises/03_log_reg_challenger"> Exercises</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/03_log_reg_challenger.ipynb'> Notebook</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/03_log_reg_challenger_solution.ipynb'> Solution</a> 
        </li>  
       </ul>
    </td>   
  </tr>
    <!--  ------------------------------------- -->
    <!--  Woche 3 -->
    <!--  ------------------------------------- -->
  <tr>
  <td>3</td>
  <td> 
	<b>Going Deeper / Tricks of the trade</b>   <a href="http://www-home.htwg-konstanz.de/~oduerr/docs/lecture03.pdf"> slides_day2</a> slides_day3</a>
  		<ul>
		<li>Fully connected network</li>
		<li>Backpropagation and Gradient Flow</li>
		<li>ReLU</li>
		<li>Regularization:
  				<ul>
  					<li>Early stopping</li>
  					<li>Dropout</li>
  				</ul>
  			</li>
  		</ul>
  </td>
  <td> 
    <ul>
      <li> <a href='http://cs231n.github.io/optimization-2/'> Backpropagation </a>  </li>
  <li> DL-book chapter 7 (for regularization)</li>
    </ul>
  </td>
  <td>
  	<ul>
	        <li>
            Multinomial Logistic Regression (forward pass, numpy, see slides) 
            <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/04_multinomial_forward_pass_solution.ipynb"> Solution</a>
        </li>
    		<li>
        		04 Multinomial Logistic Regression 
            <a href="exercises/04_Multinomial_Logistic_Regression"> Exercises</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/04_Multinomial_Logistic_Regression.ipynb'> Notebook</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/04_Multinomial_Logistic_Regression_solution.ipynb'> Solution</a> 
        </li>  	
      <li>    
        05 Fully Connected Network MNIST <a href="exercises/05_fcn_MNIST"> Exercises</a> |
		<a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/05_fcn_MNIST.ipynb'> Notebook</a> |
		<a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/05_fcn_MNIST_solution.ipynb'> Solution  </a> 
      </li>
  		<li> 06 Fully Connected network (Tricks of the Trade)
      		<a href="exercises/06_fcn_MNIST_tricks"> Exercises</a> |
		<a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/06_fcn_MNIST_keras.ipynb'> Notebook</a> |
		<a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/06_fcn_MNIST_keras_solution.ipynb'> Solution   	 </a>
     </li>
      <li>
		<a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/docs/keras-short-intro.pdf'>  Keras intro </a>	
	</li>
     </ul>
  </td>
</tr>
    <!--  ------------------------------------- -->
    <!--  Woche 4 -->
    <!--  ------------------------------------- -->
    <tr>
      <td>4</td>
      <td> 
      		<b>Convolutional Neural Networks I</b>    
		 <a href="http://www-home.htwg-konstanz.de/~oduerr/docs/lecture04.pdf"> slides_day4(pdf) </a> 
	       	 <a href="http://www-home.htwg-konstanz.de/~oduerr/docs/lecture04.ppt"> slides_day4(ppt)</a> 
      		<ul>
		        <li>Why going beyond fully connected NN?</li> 
      			<li>What is convolution?</li>      			
      			<li>Building a CNN</li>
      		</ul>
      </td>
      <td> 
        <ul>
	<li>
	<a href="https://github.com/vdumoulin/conv_arithmetic">Convolution arithmetic</a>
	</li>
	<li>
	<a href="http://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html">demo CNN and activation maps</a>
	</li>
        </ul>
      </td>
      <td>
      	<ul>
	<!--<a<li> finger-exercise ReLu/a>|-->
	<!--<a href="https://www.dropbox.com/s/yogcjidr7ng3qtb/08a-Schnelluebung-ReLu.pdf?dl=1"> Exercise</a>|-->
	<!--<a href='https://www.dropbox.com/s/d1se84xdui3uwqz/08a-Schnelluebung-ReLu-solution.pdf?dl=1'> Solution </a> -->
      	<!--</li> -->
	<li>
	<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/06b_art_lover.ipynb"> Notebook Artlover </a>|
	Homework: 07 and 08 CNN <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/docs/exercises/07_CNN_MNIST.md"> Exercises</a> |
	<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/07_cnn1_mnist.ipynb"> CNN1 Notebook </a>|
	<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/07_cnn1_mnist_solution.ipynb"> CNN1 Solution </a>|
	<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/08_cnn2_mnist.ipynb"> CNN2 Notebook </a>|		
	<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/08_cnn2_mnist_solution.ipynb"> CNN2 Solution </a>	
	</li>
	</ul>
        </td>
        </tr>
    <!--  ------------------------------------- -->
    <!--  Woche 5 -->
    <!--  ------------------------------------- -->
    <tr>
    <td>5</td>
    <td> 
    <b>Convolutional Neural Networks II</b>  <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/slides/DL-day05-presented.pdf"> slides_day5</a> 
    <ul>
    <li>What to do in case of limited data? </li>
    <li>What is a CNN looking at?</li>
    <li>Checking out challange-winning CNN architectures</li>
    <li>1D CNNs for time-ordered data</li>
    </ul>
    </td>
    <td> 
    <ul>
    <li>
    <a href="https://transcranial.github.io/keras-js/#/mnist-cnn">live CNN in browser</a>
    </li>
    <li>
    <a href="http://yosinski.com/deepvis">Understanding CNNs through visualization</a>
    </li>
    <li>
    <a href="http://cs231n.github.io/understanding-cnn/">cs231 on visualization CNNs</a>
    </li>
    <li>
    <a href="https://deepmind.com/blog/wavenet-generative-model-raw-audio/">Dilated 1D convolution</a>
    </li>
    </ul>
    </td>
    <td>
    <ul>
	    <li>
      	8 Faces Overview and FCN baseline
	<a href="https://www.dropbox.com/s/aufw2awv7s0dqm5/8_faces_dataoverview.html?dl=1"> Data overview</a>|
	<a href="exercises/09_8_faces">Exercise </a>|
	<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/09_8_faces_fc.ipynb"> FC Solution</a>
      	</li>
    <li> 
    <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/10_8_faces_cnn.ipynb"> possible CNN Solution</a> 
    </li>
    <li> 
    11 transfer learning<a href="exercises/11_8_faces_fine_tuning"> Exercises</a> |
    <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/11_8_faces_fine_tuning.ipynb"> Notebook </a>|
    <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/11_8_faces_fine_tuning_solution.ipynb"> Solution</a>
    </li>
    <!-- <li>
    13a optimized image<a href="https://www.dropbox.com/s/956jxouq0eqisn8/13-exercises-optimized-image.pdf?dl=1"> Exercise</a>|
    <a href="https://www.dropbox.com/s/5zyntjgff9k5cgm/13-exercises-optimized-image-solution.pdf?dl=1">Solution</a>|
    <a href="https://github.com/tensorchiefs/dl_course/blob/master/notebooks/13-optimize-image.ipynb"> Notebook</a>
    </li>		
    <li>
    13b adversarial example<a href="https://www.dropbox.com/s/sf8k96kxinknzfh/14-adversarial-example.pdf?dl=1"> Exercises</a> |
    <a href="https://www.dropbox.com/s/8cgm7cvr1lcqfsd/14-adversarial-example-solution.pdf?dl=1"> Solution</a>
    </li>  -->
    </ul>
   </td>
 </tr>
   <!--  ------------------------------------- -->
    <!--  Woche 6 -->
    <!--  ------------------------------------- -->
    <tr>
    <td>6</td>
     <td> 
     <b>Modern CNN Architectures and Recurent Neural Networks</b>  <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/slides/DL2019-day6-presented3.pdf"> slides_day6</a> 
     <ul>
     <li>Working with text: bag of words, embeddingss</li>
	<li>Sentiment analysis with conv1D</li>
     <li>Recurrent Neural Networks</li>
         </ul>
     </td>
     <td> 
     <ul>
     <li>Karpathy (May 2015) The unreasonable effectiveness of Recurrent Neural Networks <a href='http://karpathy.github.io/2015/05/21/rnn-effectiveness/'>(blog post)</a></li>  
      <li><a href="http://www.deeplearningbook.org/contents/rnn.html">DL-book chapter 10 </a></li>
      </ul>
      </td>
      <td>
      <ul>
      <li>
	Sentiment analysis 
	 <a href="exercises/Sentiment_analysis_with_imdb_reviews"> Exercise</a> |
	 <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/13_sentiment_analysis_with_imdb_reviews.ipynb"> Notebook </a>|
         <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/13_sentiment_analysis_with_imdb_reviews_solution.ipynb"> Solution</a>
      </li>  		
      </ul>
      </td>
    </tr>	
   <!--  ------------------------------------- -->
   <!--  Woche 7 -->
   <!--  ------------------------------------- -->
    <tr>
      <td>7</td>
      <td> 
	      <li>
       <b>Topic I: RNN continued, GRU, LSTM and Quantifying prediction uncertainties</b>   <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/slides/DL-day7-presented.pdf"> slides_day7</a> 
			      </li>
      <ul>
      <li>Using GRU</li>
      <li>Using LSTMs</li>		
      </ul>
      </td>
      <td> 
        <ul>
		 <li>Colah (August 2015) Understanding LSTM Networks <a href='http://colah.github.io/posts/2015-08-Understanding-LSTMs/'>(blog post)</a></li>
      </ul>
      </td>
      <td>
      <ul>
	      <li>
	Prediction with time series using Conv1D, RNN and LSTM
	<a href="exercises/1D_Convolutions_vs_LSTMs_and_RNNs_for_time_series"> Exercise</a> |
		<a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/12_LSTM_vs_1DConv.ipynb"> Notebook </a>|
         <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/12_LSTM_vs_1DConv_solution.ipynb"> Solution</a>
      </li>  
      </ul>
      </td>
    </tr>
   <!--  ------------------------------------- -->
   <!--  Woche 8 -->
   <!--  ------------------------------------- -->
    <tr>
      <td>8</td>
      <td> 
       	<b> Uncertainties in DL </b> <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/slides/DL-day8-plan3.pdf"> slides_day8</a>
      <ul>
      <li> Recap: Modeling uncertainties in simple linear regression </li>
      <li> MC Dropout to quantify uncertainties in DL models</li>		
      </ul>
      </td>
      <td> 
        <ul>
	<li><a href="http://mlg.eng.cam.ac.uk/yarin/blog_3d801aa532c1ce.html">What My Deep Model Doesn't Know</a>
        </li>
      </ul>
      </td>
      <td>
      <ul>
	            <li>		
         MC-Dropout on Cifar10 <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/17_cifar10_not_all_labels_MC_Dropout.ipynb"> Notebook </a>|
         <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/17_cifar10_not_all_labels_MC_Dropout_solution.ipynb"> Solution</a>
      </li>
	            <li>		
        Linear Regression with TF Probability <a href="https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/18_TFP_Regression.ipynb"> Notebook </a>
      </li>
	  </ul>    
      </td>
    </tr>
</table>  
 













Tensorchiefs are Oliver Dürr, Beate Sick and Elvis Murina.

