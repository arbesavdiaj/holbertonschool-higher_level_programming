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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
