django-sandbox
==============

A simple Django sandbox leveraging importd.

Quick Setup
-----------

After cloning the project, the following commands will get a
development server up and running.

    virtualenv --distribute .
    . bin/activate
    ./server

Usage
-----

Using this project is relatively simple. By default, it uses
SQLite as it's database engine. After cloning, you should
either create a virtualenv in the sandbox directory:

    virtualenv --distribute .
    . bin/activate
  
If you prefer to use virtualenvwrapper, go ahead and make one
with that:

    mkvirtualenv sandbox
    workon sandbox

Now that you've created and activate your virtualenv, go ahead
and install the dependencies for this repository:

    pip install -r requirements.txt
    
After these are installed, you will want to do some initial
setup.

    ./server syncdb

Now, you can run a Django development server with ease:

    ./server

