README
======

Interacting with EC2 instances
==============================

Options to interact with EC2 instances:

1. A standalone SSH client 
2. EC2 Instance Connect (browser-based SSH connection) 
3. A Java SSH Client directly from my browser (Java required) 

In the context of SMM635/638, students are required to go for option 1
 (describe below) 

Standalone SSH client
---------------------

To access your instance:

1. Open an SSH client. (find out how to connect using PuTTY)

2. Locate your private key file (```your_key.pem```). The wizard
 automatically detects the key you used to launch the instance. Your key
  must not be publicly viewable for SSH to work. Use this command if needed:

```bash
$ chmod 400 your_key.pem
```

3. Connect to your instance using its Public DNS, e.g.: ```xxx-xx-xxx-xx-xx.eu-west-2.compute.amazonaws.com```

Example:

```bash
$ ssh -i "Users/you/your_key.pem" ubuntu@ec2-xx-xxx-xx-xx.eu-west-2.compute.amazonaws.com
```

Installing Anaconda
===================

Download Anaconda from the command line:

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
```
Run the installer:

```bash
$ bash Anaconda3-2019.10-Linux-x86_64.sh
```
At this point, just follow the instructions reported by the interactive
 installer:

- press ```return``` to start the installation procedure
- fully display the license agreement (press ```space``` multiple times to
  scroll-down) and accept it
- you may want to install Anaconda in the default folder ```/home/ubuntu
/anaconda3```
- reply ```yes``` when the installer asks to initialize Anaconda 3 

Anconda has been installed. In order to make the command available to your
 terminal session run (once for all) what follows:
 
```bash
$ source .bashrc
```

Running Python code on AWS servers
==================================

MacOS and Linux users can SSH tunnel to AWS servers as follows:  (see [details](https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server))

```bash
$ ssh -i "your_key.pem" -L 8000:localhost:8888 ubuntu@ec2-xx-xxx-xx-xx.eu:w-west-2.compute.amazonaws.com
```

Now you start a Jupyter server:

```bash
$ jupyter notebook --no-browser
```

On your client browser, you open ```localhost:8000```, where Jupyter is
 accessible. 

It is also possible to run Python code from within Pycharm. To do that, it
 is necessary to add a new Python interpreter to the project:
  
- go to 'Settings' (Windows/Linux users) or 'Preferences' (MacOS users)
  users), then search for 'Project interpreter'
- add a new SSH interpreter
- a new dialogue box pops up: As user place 'ubuntu'; as
   address pass the public DNS of the server; in the next step, load your
    ```.pem``` key from the file.
    
The console of your Pycharm shows the IPython/Python session ongoing in the
 AWS server.
