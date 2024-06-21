#!/usr/bin/python3
"""Lists all states in a database"""

import MySQLdb
import sys


def list_states(username, password, database_name, search):
    """Connects to MySQL server"""

    try:
        conn = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=username,
                               password=password,
                               db=database_name)
        cursor = conn.cursor()
        query = "SELECT name FROM hbtn_0e_4_usa.cities\
                 WHERE state_id = (\
                     SELECT state.id FROM hbtn_0e_4_usa.states\
                     WHERE name = %s)\
                 ORDER BY id ASC"

        cursor.execute(query, (search,))
        cities = cursor.fetchall()
        for city in cities:
            print(city)
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connectig to MySQL or execuiting query: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 file username password database search")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        search = sys.argv[4]
        list_states(username, password, database_name, search)
