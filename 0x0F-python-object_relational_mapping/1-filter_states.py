#!/usr/bin/python3
"""
A script that lists states with a name starting
with 'N' from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8')
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
