#!/usr/bin/python3
import MySQLdb

def connect_to_mysql(username, password, database_name):
    """Connects to MySQL server"""
    
    try:
        conn = MySQLdb.connect(host="localhost",
                            port="33060",
                            user=username,
                            password=password,
                            db=database_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM staes ORDER BY states.id ASC")
        
        states = cursor.fetchall()
        
        for state in states:
            print(state)
            
        cursor.close()
        conn.close
        
    except MySQLdb.Error as e:
        print(f"Error connectig to MySQL or execuiting query: {e}")