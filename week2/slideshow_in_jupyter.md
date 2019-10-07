Slideshows in Jupyter
======================

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: created on Mon  7 Oct 18:58:10 2019


Overview
========

Thanks to the [RISE](https://rise.readthedocs.io/en/maint-5.5/installation.html)
extension, it is possible to create elegant and dynamic
slide-shows from within Jupyter. The main advantage 

This simple README doesn't pretend to substitute the great documentation
provided by the RISE project. Rather, it provides a concise step-by-step
approach to get RISE work on your Anaconda installation.


Steps
=====

If the Jupyter extension manager is not installed on your machine, go first through
steps 1-3. Otherwise go to step 4.

1. Activate the relevant ```conda``` environment (e.g., smm635)
2. Install the Jupyter extension manager as follows by running ```conda install 
  -c conda-forge jupyter_contrib_nbextensions```
3. Install javascript and css files with ```jupyter contrib nbextension install --user```
4. Install RISE with ```conda install -c conda-forge rise```

The next time you launch a Jupyter server instance (from within smm635), the RISE 
option should be visible under the 'extensions' tab. The 'usage' section included 
in the RISE documentation page is a good place to start to fully profit from this 
great extension.
