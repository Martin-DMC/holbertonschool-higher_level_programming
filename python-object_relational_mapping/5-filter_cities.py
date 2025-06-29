#!/usr/bin/python3
"""
this module a script that list all cities of the database
hbtn_0e_4_usa, connecting with a server local MySQL
"""
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    usr = argv[1]
    pswd = argv[2]
    datab = argv[3]
    state_name = argv[4]

    db = None
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=usr,
            passwd=pswd,
            db=datab
        )
        cur = db.cursor()
        query = "SELECT c.name\
                 FROM cities AS c\
                 JOIN states AS s ON c.state_id = s.id\
                 WHERE s.name = %s\
                 ORDER BY c.id ASC;"
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
        for i, row in enumerate(rows):
            if i == 0:
                print(f"{row[0]}", end='')
            else:
                print(f", {row[0]}", end='')
        print("")
    except MySQLdb.Error as e:
        print(f"{e}")
        sys.exit(1)
    finally:
        if db:
            db.close()
