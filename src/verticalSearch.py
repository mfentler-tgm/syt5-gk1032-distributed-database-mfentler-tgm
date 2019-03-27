#!/usr/bin/python
import psycopg2
from config import config
import sys

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config('postgresql:vertical')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT * FROM vertikal.simplefilm;')

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
        params = config('postgresql:vertical')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('Number of columns in vertical table:')
        cur.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_SCHEMA = 'vertikal' AND TABLE_NAME = 'simplefilm';")
        dvds = cur.fetchall()
        for x in dvds:
            print(x)

        print('Number of columns in the rest table:')
        cur.execute("SELECT count(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_SCHEMA = 'vertikal' AND TABLE_NAME = 'simplefilm_rest';")
        dvds = cur.fetchall()
        for x in dvds:
            print(x)

        print('Creating the merged table:')
        cur.execute('DROP TABLE IF EXISTS vertikal.simplefilm_merged;')
        cur.execute('CREATE TABLE vertikal.simplefilm_merged AS (SELECT vertikal.simplefilm.prod_id, special,common_prod_id,actor,category,price,title FROM vertikal.simplefilm,vertikal.simplefilm_rest WHERE vertikal.simplefilm.prod_id = vertikal.simplefilm_rest.prod_id);')

        print('Number of columns in the merged table:')
        cur.execute("SELECT count(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = 'ds2' AND TABLE_SCHEMA = 'vertikal' AND TABLE_NAME = 'simplefilm_merged';")
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
    #connect()
    ek()