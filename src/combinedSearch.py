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
        print('Number of columns in combined table:')
        cur.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_SCHEMA = 'combination' AND TABLE_NAME = 'cheap_comedy_simplified';")
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of columns in the standard table:')
        cur.execute("SELECT count(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_NAME = 'products';")
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of columns in the standard table without the excluded values:')
        cur.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_NAME = 'products' AND COLUMN_NAME NOT IN (SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_SCHEMA = 'combination' AND TABLE_NAME = 'cheap_comedy_simplified');")
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of entries in combined table:')
        cur.execute('SELECT count(*) FROM combination.cheap_comedy_simplified;')
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of entries in the standard table:')
        cur.execute('SELECT count(*) FROM products;')
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of entries in the standard table without the excluded values:')
        cur.execute('SELECT count(*) FROM products WHERE prod_id NOT IN (SELECT prod_id FROM combination.cheap_comedy_simplified);')
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
if __name__ == '__main__':
    connect()
    ek()