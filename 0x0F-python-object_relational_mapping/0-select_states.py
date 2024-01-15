#!/usr/bin/python3
"""A script to list all the states from the database htbn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    host = "localhost"
    port = 3306
    username = argv[1]
    password = argv[2]
    data_name = argv[3]

    with MySQLdb.connect(host, username, password, data_name, port) as database:
        with database.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER.id ASC")
            table_rows = cur.fetchall()
            for state in table_rows:
                print(state)
