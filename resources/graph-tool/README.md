Install Graph-tool
==================

Via Conda
---------

This option is available to Linux and MacOS users only. First, add three new
 channels (if not present):

```shell script
$ conda config --add channels conda-forge
$ conda config --add channels pkgw-forge
```

Then, install the following packages (in this order):

```shell script
$ conda install -c pkgw-forge gtk3
$ conda install -c conda-forge pygobject
$ conda install -c conda-forge  matplotlib
$ conda install -c conda-forge graph-tool
```

Open a Python console in this environment and type:
  
```python
from graph_tool.all import *
``` 

If the import goes fine, graph-tool is properly installed.


Get the Docker Image of Graph-tool (recommended)
------------------------------------------------

### Pull the image

The most hands-off and OS-agnostic way to install graph-tool is using Docker. 
If you have Docker installed, this can be done simply by running:

```shell script
docker pull tiagopeixoto/graph-tool
```

This will download a Docker image based on Arch GNU/Linux, that contains
 graph-tool, and can be run in any modern GNU/Linux distribution, MacOS X and 
 Windows. It contains some other useful Python packages, such as Matplotlib, 
 Pandas, IPython and Jupyter.

### Interactive sessions
After the image is pulled, you can start an interactive python shell in the 
container by running:

```shell script
docker run -it -u user -w /home/user tiagopeixoto/graph-tool ipython
```

which will give you a Python 3 environment with graph-tool installed:

```
Python 3.6.5 (default, May 11 2018, 04:00:52) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from graph_tool.all import *
In [2]: 
```

### Interactive visualizations
If you want to use interactive visualization from within docker, you have first 
to enable local connections to the X server:

```shell script
xhost +local:
```

and then run the container with

```shell script
docker run -ti -u user -w /home/user --rm -e DISPLAY=$DISPLAY -v /tmp
/.X11 -unix:/tmp/.X11-unix tiagopeixoto/graph-tool ipython
```

### Jupyter notebooks

To run jupyter notebooks from inside the docker image, you need to forward the 
necessary ports to the container, so that your native browser can connect to it at http://localhost:8888/. 
You need first to start an interactive shell session

```shell script
docker run -p 8888:8888 -p 6006:6006 -it -u user -w /home/user tiagopeixoto/graph-tool bash
```

and then start the notebook server

```shell script
[user@c20b92b8c4bf ~]$ jupyter notebook --ip 0.0.0.0
```

Do not forget to connect to `http://localhost:8888/` instead of `http://0.0.0.0:8888/`, 
otherwise the connection to the kernel will not work!
(MacOS and Windows users still need to bind the above ports in the VM, as
 described [here](https://stackoverflow.com/questions/33636925/how-do-i-start-tensorflow-docker-jupyter-notebook))