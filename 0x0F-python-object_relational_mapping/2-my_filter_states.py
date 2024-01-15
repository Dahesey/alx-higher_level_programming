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
            charset='utf8')
    with db.cursor() as cursor_obj:
        query = """SELECT * FROM states WHERE BINARY
        name = '{}' ORDER BY id ASC""".format(search)
        cursor_obj.execute(query)
        fetched_state = cursor_obj.fetchall()
        for state in fetched_state:
            print(state)

