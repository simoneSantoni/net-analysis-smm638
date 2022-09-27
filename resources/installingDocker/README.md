Install Docker Engine (Community Edition) - README
==================================================

Docker for Ubuntu 
-----------------

You can install Docker Engine - Community in different ways, depending on your needs:

Most users set up Docker’s repositories and install from them, for ease of installation and upgrade tasks. This is the recommended approach.

Some users download the DEB package and install it manually and manage upgrades completely manually. This is useful in situations such as installing Docker on air-gapped systems with no access to the internet.

In testing and development environments, some users choose to use automated convenience scripts to install Docker.

Install using the repository
Before you install Docker Engine - Community for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.

### Step 1 - SET UP THE REPOSITORY

Update the apt package index:

    $ sudo apt-get update

Install packages to allow apt to use a repository over HTTPS:

    $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common

Add Docker’s official GPG key:

    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

    $ sudo apt-key fingerprint 0EBFCD88

Use the following command to set up the stable repository:

    $ sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
 

### Step 2 - INSTALL DOCKER ENGINE - COMMUNITY

Update the apt package index.

    $ sudo apt-get update

Install the latest version of Docker Engine - Community and containerd, or go to the next step to install a specific version:

    $ sudo apt-get install docker-ce docker-ce-cli containerd.io

Verify that Docker Engine - Community is installed correctly by running the hello-world image.

    $ sudo docker run hello-world

### Step 3 - FOR WINDOWS USERS RUNNING UBUNTU IN THE SUB-SYSTEM

When Windows users try to run the previous command, they get the following
 error: 
 
     Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the 
     docker daemon running?

This [Medium post](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4) 
shows how to deal with the problem.

*Ditto*, in the interest of installing Graph-Tool, Windows users can also
 use Conda to get the library work in their Ubuntu sub-system. 

Docker for MacOS
----------------

Download and run the [graphical installer](https://docs.docker.com/docker-for-mac/install/). Registration required.

Once the software is installed, try to launch Docker from the icon.


Docker for Win10
----------------

If you have a copy of Win10 'Pro' or 'Enterprise', download and run the [graphical installer](https://docs.docker.com/docker-for-windows/install/). Registration required. If you have Win10 Home, just use Ubuntu.
