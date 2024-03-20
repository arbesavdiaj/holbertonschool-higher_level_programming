#!/usr/bin/python3
"""
Filter states by user Input
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """displays all values in the table where name matches the argument"""
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    x = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s \
                ORDER BY states.id", (x, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
