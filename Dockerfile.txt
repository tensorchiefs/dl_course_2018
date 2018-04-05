#FROM tensorflow/tensorflow:latest-gpu-py3
FROM tensorflow/tensorflow:latest-py3
#FROM tensorflow/tensorflow:1.0.0-gpu-py3
# Removing some notebook which caused confusion
RUN rm /notebooks/1_hello_tensorflow.ipynb
RUN rm /notebooks/2_getting_started.ipynb
RUN rm /notebooks/3_mnist_from_scratch.ipynb

MAINTAINER oliver duerr <dueo@zhaw.ch>

RUN pip --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        pandas \
        h5py \
        keras \
        tflearn \
        ggplot

# RUN pip --no-cache-dir install tflearn
# RUN pip install git+https://github.com/tflearn/tflearn.git
# RUN pip install keras

RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list'
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
RUN gpg -a --export E084DAB9 | apt-key add -

RUN apt-get update && apt-get install -y git
RUN apt-get -y install r-base
# Pydot for Keras for Beate
RUN apt-get -y install python-pydot python-pydot-ng graphviz #For Keras model visualization
RUN pip3 install pydot
RUN pip3 install graphviz

#RUN apt-get install libzmq3-de
RUN pip3 install rpy2

# jupyterlab
RUN pip install jupyterlab

# For toc in notebook
RUN pip install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN pip install jupyter_nbextensions_configurator

# Clean
RUN apt-get clean && \
rm -rf /var/lib/apt/lists/*

# Some nice stuff for R
RUN R -e "install.packages('tidyverse', repos = 'https://cloud.r-project.org')"

# Default directory that will be saved by htcondor
#RUN mkdir /tmp/results
#RUN nvidia-smi -f /tmp/temp.txt

# COPY -> to copy files/data from to localmachine
COPY notebooks /notebooks

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/notebooks"
COPY notebooks /notebooks


COPY run_jupyter_2.sh /
COPY run_jlab.sh /

CMD ["/run_jupyter_2.sh"]
