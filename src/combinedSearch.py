#!/usr/bin/python
import psycopg2
from config import config
import sys

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config('postgresql:combined')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('Data in combined table:')
        cur.execute('SELECT * FROM combination.cheap_comedy_simplified;')

        # display the PostgreSQL database server version
        dvds = cur.fetchall()
        for x in dvds:
            print(x)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def ek():
    pass

if __name__ == '__main__':
    connect()