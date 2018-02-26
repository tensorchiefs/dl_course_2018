---
layout: default
title: Deep Learning Course 
---
# Deep Learning (CAS machine intelligence) 

This course in deep learning focuses on practical aspects of deep learning. 

For the hands-on part you could install anaconda ([details and installation instruction](anaconda.md)) or use the provided a docker container ([details and installation instruction](docker.md)).

To easily follow the course please make sure that you are familiar with the some [basic math and python skills](prerequistites.md). 

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
    <td>Tue Feb 20</td>
    <td>13:30-17:00</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Tue Feb 27</td>
    <td>13:30-17:00</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Tue March 06</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Tue March 13</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Tue March 20</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Tue March 27</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Tue April 03</td>
    <td>09:00-12:30</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Tue April 10</td>
    <td>13:30-17:00</td>
  </tr>
</table>
<p>&nbsp;</p> <!-- leerer absatz -->

  
## Syllabus 

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
        <b>Deep learning basics</b> <a href="https://www.dropbox.com/s/z05k981kx0oechm/lecture01.pdf?dl=1">slides</a>
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
       <b>Gradient Descent and loss functions for classification</b> <a href="https://www.dropbox.com/s/lurmsqh1exedtkk/lecture02.pdf?dl=1">slides</a>
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
        <li>
            Multinomial Logistic Regression (forward pass, numpy, see slides) 
            <a href="exercises/04_multinomial_forward_pass_solution"> Solution</a>
        </li>
    		<li>
        		04 Multinomial Logistic Regression 
            <a href="exercises/04_Multinomial_Logistic_Regression"> Exercises</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/04_Multinomial_Logistic_Regression.ipynb'> Notebook</a> |
            <a href='https://github.com/tensorchiefs/dl_course_2018/blob/master/notebooks/04_Multinomial_Logistic_Regression_solution.ipynb'> Solution</a> 
        </li>         
      </ul>
    </td>   
  </tr>
</table>
 















Tensorchiefs are Oliver Dürr, Beate Sick and Elvis Murina.

