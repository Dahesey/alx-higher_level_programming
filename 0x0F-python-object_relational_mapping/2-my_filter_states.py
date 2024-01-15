#!/usr/bin/python3

"""
A script thata takes in an argument and display all values
in the states table of hbtn_0e_0_usa where name matches argument"""

if __name__ == "__main__":
    
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            state_name = sys.argv[4],
            charset='utf8')
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)
        cursor.close()
        db.close()
