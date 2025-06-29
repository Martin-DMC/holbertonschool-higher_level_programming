#!/usr/bin/python3
"""
this module a script  that list all states
(if they comply with requirement) of the database
hbtn_0e_usa, connecting with a server local MySQL
"""
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    usr = argv[1]
    pswd = argv[2]
    datab = argv[3]

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
        cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'\
                     ORDER BY id ASC;")
        rows = cur.fetchall()
        for row in rows:
            print(f"({row[0]}, '{row[1]}')")
    except MySQLdb.Error as e:
        print(f"{e}")
        sys.exit(1)
    finally:
        if db:
            db.close()
