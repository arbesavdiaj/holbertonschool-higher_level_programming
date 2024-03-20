#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

def list_states(username, password, database):
    """Connects to the MySQL server and lists all states"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        exit(1)
    list_states(argv[1], argv[2], argv[3])
