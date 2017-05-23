# Logs-Analysis
This project is part of the Full Stack Web Developer nanodegree from udacity.

## The purpose of this project
Building an informative summary from logs is a real task that comes up very often in software engineering. The project utilizes [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197) to design a database based off of a provided specification and use case and then write code that makes use of that data with Python prgramme and PostgreSQL database.

## Prerequirements
This project requires Python 2.X (2.7.x is expected) and PostgreSQL 9.3 or latest version.
[Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) are required to run SQL database server and web app. [Download database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to get report. You need to install them on your machine.

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
This file contains the table and views definition for the project.
- report.txt
This file is the result of analyzed log data from the database

## Commands
The following SQL statements are to create views to answer the questions.
To answer the question 2, execute following lines to create view.  
`CREATE VIEW viewer AS SELECT author, count(log.path) AS num \
               FROM articles, log WHERE articles.slug = substring(path from \
               10 for 100) GROUP BY author ORDER BY num DESC LIMIT 4;`  
This statements mean that "Create view to find relationships between authors and relevant logs".

To answer the question 3, execute following 2 lines to create view.  
`CREATE OR REPLACE VIEW error AS SELECT \
            to_char(time, 'Mon DD, YYYY') as date, \
            count(status) AS err, status FROM log \
            WHERE status = '404 NOT FOUND' GROUP BY date\
            , status ORDER BY date ASC;`  
This statements mean that "Create view to count the number of 404 NOT FOUND status".

`CREATE OR REPLACE VIEW total AS SELECT \
            to_char(time, 'Mon DD, YYYY') as date, count(status) AS total\
            FROM log GROUP BY date ORDER BY date ASC;`  
This statements mean that "Create view to count the number of all status".

## Code Quality
[Here](https://google.github.io/styleguide/pyguide.html) is the Google Python Style Guide that I followed.
