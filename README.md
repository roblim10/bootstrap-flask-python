Python Flask Bootstrap Project
===
About this project
---

This is a basic web application that implements the "Handshake Bootstrap" spec specified for our 
interviews.  This stack is based off of [Flask](http://flask.pocoo.org/), a microframework for building
simple web applications using Python.

The database this project uses is a SQLite database.  The database file is located at 
the root level directory called `handshake-interview.db`.  There exists one table called `alarms` that has two 
records, as described in the "Handshake Bootstrap" spec.

Install Python 3
---
Make sure you have Python 3 installed in order to run this project.  [This article](https://docs.python-guide.org/starting/install3/osx/) 
provides a good method to install Python 3 via Homebrew (recommended).  On Windows, you can download the Python installer
[here](https://www.python.org/downloads/).

Setting up a virtual environment
---
It's best you create a Python virtual environment in this project.  Run `python -m venv venv` to create a directory
called `venv` that will manage your project environment.  You can now run `source venv/bin/activate` in the root
directory to say you want to use the virtual environment

Set up the project dependencies
---
At the root of this project, there is a `requirements.txt` file that you can use to install all the Python dependencies
you need.  While your virtual environment is activated, run `pip install -r requirements.txt` to install all
the dependences inside the virtual environment.

Running the project
---
Once all dependencies are installed, you can run the following commands to start the server:
```
export FLASK_APP=bellbird.py
flask run
```

The server should start with an output that looks something like this:
```
 * Serving Flask app "bellbird.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Once the server has started, go to http://127.0.0.1:5000 in your browser and you should see the application from the
"Handshake Bootstrap" spec.

Having trouble?
---
If you are having trouble getting this project set up, we encourage you to look at 
[this tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), which provides a good 
explanation of what the above commands are doing.  If you are still having trouble getting the application up and running,
please email your recruiter and a Handshake engineer can help you troubleshoot what is going wrong.

What to do
====
During the Handshake interview process, we will ask you to modify this project to implement features and build out a fully
functioning web application.  We may also ask you to explain the code that you have written and/or explain how this 
web framework works, so please be sure to study the code in this project.  If you are not completely familiar with the 
Flask framework, we recommend you read through the documentation and make sure you understand how to work with it.

You are free to modify this web stack to use any technologies you would like to use.