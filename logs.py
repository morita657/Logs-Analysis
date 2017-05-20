#
# Database access functions for the newsdata.
#
import time
import psycopg2

box = []
DBNAME = "newsdata"
def popular_articles():
    f = open("report.txt", "w")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    f.write('1. What are the most popular three articles of all time?\n')
    # Find articles and their number of views
    cur.execute("SELECT title, count(path) AS num FROM articles, \
                 log WHERE articles.slug = substring(path from 10 for 100)\
                 GROUP BY title ORDER BY num DESC LIMIT 3;")
    results = cur.fetchall()
    for line in results:
        print "q1: ", line
        f.write('"' + str(line[0]) + '" - ' + str(line[1]) + ' views' + '\n')
    db.close()

def popular_authors():
    f = open("report.txt", "a")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    f.write('\n2. Who are the most popular article authors of all time?\n')
    # Create view to find relationships between authors and relavant logs
    cur.execute("CREATE VIEW viewer AS SELECT author, count(log.path) AS num \
                 FROM articles, log WHERE articles.slug = substring(path from \
                 10 for 100) GROUP BY author ORDER BY num DESC LIMIT 3;")
    # Find authors and count his/her articles views
    cur.execute("SELECT a.name, v.num \
                 FROM authors AS a\
                 INNER JOIN viewer AS v ON v.author = a.id \
                 GROUP BY a.name, v.num \
                 ORDER BY v.num DESC;")
    results = cur.fetchall()
    for line in results:
        print "q2: ", line
        f.write('"' + str(line[0]) + '" - ' + str(line[1]) + ' views' + '\n')
    db.close()

def error_status():
    f = open("report.txt", "a")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    f.write('\n3. On which days did more than 1% of requests lead to errors?\n')
    # Create view to count the number of 404 NOT FOUND status
    cur.execute("CREATE OR REPLACE VIEW error AS SELECT \
                 to_char(time, 'Mon DD, YYYY') as date, \
                 count(status) AS err, status FROM log \
                 WHERE status = '404 NOT FOUND' GROUP BY date\
                 , status ORDER BY date ASC;")
    # Create view to count the number of all status
    cur.execute("CREATE OR REPLACE VIEW total AS SELECT \
                 to_char(time, 'Mon DD, YYYY') as date, count(status) AS total\
                 FROM log GROUP BY date ORDER BY date ASC;")
    # Put together both views to get relationship between date and the rate of 404 NOT FOUND status
    cur.execute("SELECT e.date, (e.err/t.total::float)*100 \
                 FROM total AS t \
                 LEFT OUTER JOIN error AS e ON e.date = t.date \
                 ORDER BY date ASC;")
    results = cur.fetchall()
    for line in results:
        if line[1] >= 1:
            print "more than 1%: ", str(line[1])[0:3]
            f.write('"' + str(line[0]) + '" - ' + str(line[1])[0:3] + '% errors'\
                    + '\n')
    db.close()



# CREATE OR REPLACE VIEW error AS SELECT to_char(time, 'Month DD, YYYY') as date, count(status) AS err, status FROM log WHERE status = '404 NOT FOUND' GROUP BY date, status ORDER BY date ASC;
#
# CREATE OR REPLACE VIEW total AS SELECT to_char(time, 'Month DD, YYYY') as date, count(status) AS total FROM log GROUP BY date ORDER BY date ASC;

# SELECT e.date, e.err/sum(status) as total \
# FROM log AS l \
# INNER JOIN error AS e ON e.date = l.date \
# ORDER BY date ASC;

#
#
# SELECT e.date, e.err/sum(status) as total FROM log AS l INNER JOIN error AS e ON e.date = l.date ORDER BY e.date ASC;


popular_articles()
popular_authors()
error_status()
