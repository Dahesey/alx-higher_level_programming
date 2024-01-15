#!/usr/bin/python3
"""A script to list all the states from the database htbn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            data=argv[3],
            charset='utf8')
    cu = data.cursor()
    cu.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cu.fetchall()]
    cu.close()
    data.close()
