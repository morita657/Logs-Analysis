# Logs-Analysis
This project is part of the Full Stack Web Developer nanodegree from udacity.

## The purpose of this project
Building an informative summary from logs is a real task that comes up very often in software engineering. The project utilizes [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197) to design a database based off of a provided specification and use case and then write code that makes use of that data with Python prgramme and PostgreSQL database.

## Prerequirements
This project requires Python 2.X (2.7.x is expected) and PostgreSQL 9.3 or latest version.
[Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) are required to run SQL database server and web app. You need to install them on your machine.

## How to run
1. Download or clone repository on you machine.
2. Bring the project directory under the vagrant directory.
3. Start the virtual machine using `vagrant up` command.
4. After that, run `vagrant ssh` to log in to your VM.
5. Go to logs directory with `cd /vagrant/logs`.
6. Run logs.py file to analyse the log data from the database using `python logs.py`.
7. Go to report.txt file to discover what kind of article's the site's readers like.
8. Shutdown the VM with `CTRL + D`.

## Files
This project is comprised of 3 files:
- logs.py	 
This file contains the implementation of internal reporting tool
- newsdata.sql
This file contains the table definition for the project
- report.txt
This file is the result of analyzed log data from the database

## Code Quality
[Here](https://google.github.io/styleguide/pyguide.html) is the Google Python Style Guide that I followed.
