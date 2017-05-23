#
# Database access functions for the newsdata.
#
#! /usr/bin/env python
import time
import psycopg2

box = []
DBNAME = "newsdata"


def popular_articles():
    f = open("report.txt", "w")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    f.write('Most popular articles:\n')
    # Find articles and their number of views
    cur.execute("SELECT title, count(path) AS num FROM articles, \
                 log WHERE articles.slug = substring(path from 10 for 100)\
                 GROUP BY title ORDER BY num DESC LIMIT 3;")
    results = cur.fetchall()
    for line in results:
        print "q1: ", line
        f.write("{} - {} views\n".format(str(line[0]), str(line[1])))
        print("-" * 70)
    db.close()


def popular_authors():
    f = open("report.txt", "a")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    f.write('\nMost popular authors:\n')
    # Find authors and count his/her articles views
    cur.execute("SELECT a.name, v.num \
                 FROM authors AS a\
                 INNER JOIN viewer AS v ON v.author = a.id \
                 GROUP BY a.name, v.num \
                 ORDER BY v.num DESC;")
    results = cur.fetchall()
    for line in results:
        print "q2: ", line
        f.write("{} - {} views\n".format(str(line[0]), str(line[1])))
        print("-" * 70)
    db.close()


def error_status():
    f = open("report.txt", "a")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    f.write('\nDays with more than 1% errors:\n')
    # Put together both views to get relationship between date
    # and the rate of 404 NOT FOUND status
    cur.execute("SELECT e.date, (e.err/t.total::float)*100 \
                 FROM total AS t \
                 LEFT OUTER JOIN error AS e ON e.date = t.date \
                 ORDER BY date ASC;")
    results = cur.fetchall()
    for line in results:
        if line[1] >= 1:
            print "more than 1%: ", str(line[1])[0:3]
            f.write("{} - {}% errors\n".format(str(line[0]),
                    str(line[1])[0:3]))
            print("-" * 70)
    db.close()
popular_articles()
popular_authors()
error_status()
