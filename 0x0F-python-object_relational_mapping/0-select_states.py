#!/usr/bin/python3
"""A script to list all the states from the database htbn_0e_0_usa"""

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
    cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cursor.fetchall()]
    cursor.close()
    db.close()
