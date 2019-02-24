## Previous Knowlegde

To follow the course some prerequisites are required. 


### Math calculus

* Matrix Algebra 

Most algorithms in deep learning are based on matrix algebra and GPUs are often used since they are especially fast in performing matrix operations. Therefore basic knowledge of matrix algebra is needed to understand deep learning algorithms.  A good overview can be found at [http://www.souravsengupta.com/cds2016/lectures/Savov_Notes.pdf](http://www.souravsengupta.com/cds2016/lectures/Savov_Notes.pdf) you will only need the first two pages - stuff like Eigenvalues and basis expansion are note strictly required for the course.

* Calculus

You should know the chain rules, since it is the core of the back propagation algorithm. For a refresher check out e.g. [Wikipedia](https://en.wikipedia.org/wiki/Chain_rule) or for an alternative approach the following [link](https://betterexplained.com/articles/derivatives-product-power-chain/)

* Statistics

You should know the basic descriptive statistics (mean, standart deviation, median, z-transformation) and have a solid understanding of probability and e.g. know that P(A\|B) refers to the probability of event A given that event B was observed and P(A\|B)=P(A) in case of A and B are independent. You should also be familiar with some calculus like P(A,B)= P(A\|B) P(B). You might consider the following [cheat sheet](http://web.mit.edu/~csvoss/Public/usabo/stats_handout.pdf) (tests are not required). 

### Computer stuff

* Python and Jupyter Notebooks

You need a basic knowledge of python, see e.g. [datacamp python cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PythonForDataScience.pdf). We will use jupyter notebooks and make use of numpy, matlibplot and of course the deep learning libraries TensorFlow, and Keras. To get an introduction how to work with jupyter notebooks, see for example this [jupyter intro webpage](https://jupyter.org/try).

For the hands-on part you can work via colab which does not require any installation - for getting started with colab follow the [instructions how to use google colab](co.md). Or you can use the provided a docker container ([details and installation instruction](docker.md)), or install anaconda ([details and installation instruction](anaconda.md)) or .

