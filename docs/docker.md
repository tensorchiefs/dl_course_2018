# How to use the docker container for the course

** Note that it's also possible to use a TensorFlow installation with anaconda, this is especially important for windows users which sometimes struggle quite a lot to install docker **

We provide a docker image [oduerr/tf_docker:cpu_r](https://github.com/oduerr/tf_docker) with [Tensorflow](http://www.tensorflow.org) (v1.5.0) , [TFLearn](http://tflearn.org/), [Keras](https://keras.io/), and many other pre-installed python libraries (numpy, pandas). It also allows to run R-code inside the notebooks. See e.g. [here](https://github.com/oduerr/tf_docker/blob/cpu_r/notebooks/UseR.ipynb) how to use it.

## Installation of docker

* The official installation guide can be found at: [https://docs.docker.com/engine/installation/](https://docs.docker.com/engine/installation/)
* In case that the docker installation does not work you can directly install Tensorflow via Anaconda. You can find an installation guide on our website: [Anaconda installation guide](https://github.com/tensorchiefs/dl_course_2018/blob/master/docs/anaconda.md)


## Running the container
In the docker command line execute:

```
docker run -p 8888:8888 -p 6006:6006 -it oduerr/tf_docker:cpu_r
```
open [http://localhost:8888/?token=tensorchiefs](http://localhost:8888/?token=tensorchiefs) or [http://192.168.99.100:8888/tree?token=tensorchiefs](http://192.168.99.100:8888/tree?token=tensorchiefs)(for windows) in the browser. 

## Running with a linked file system.
If you want to access a directory here (/Users/oli/Documents/workspace/dl_tutorial/) from inside the docker container execute:

```
docker run -p 8888:8888 -p 6006:6006 -v /Users/oli/Documents/workspace/dl_tutorial/:/notebooks/local/ -it oduerr/tf_docker:cpu_r
#or for windows users
docker run -p 8888:8888 -p 6006:6006 -v /c/Users/Elvis/Desktop/:/notebooks/ -it oduerr/tf_docker:cpu_r

```


## Updating
Please make sure to use the latest container by updating it using 

```
docker pull oduerr/tf_docker:cpu_r
```

## Other useful hints for docker

### Starting in bash
In case you want to not start the jupyter notebook sever automatically but want a bash shell do:

```
docker run -p 8888:8888 -p 6006:6006 -it oduerr/tf_docker:cpu_r bash
```

### Local vs Inside container
The entry before the colon ':' is on the local machine, the one after it inside the container. Examples:

```
  docker run -p 4242:8888 -it oduerr/tf_docker:cpu_r #4242 is the port on the local machine, 8888 inside the container
  docker run -v /tmp/dl_tutorial/:/notebooks/dl_tutorial/ #/tmp/dl_tutorial is on local machine
```














