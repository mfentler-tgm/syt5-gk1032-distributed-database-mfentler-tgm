#!/usr/bin/python
import psycopg2
from config import config
import sys

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config('postgresql:horizontal')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT * FROM horizontal.cheap_comedy;')
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
        params = config('postgresql:horizontal')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('Number of entries in horizontal fragment table:')
        cur.execute('SELECT count(*) FROM horizontal.cheap_comedy;')
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of entries in rest table:')
        cur.execute('SELECT count(*) FROM horizontal.cheap_comedy_rest;')
        dvds = cur.fetchall()
        for x in dvds:
            print(x)
        print('Number of entries in the combined table:')
        cur.execute('DROP TABLE IF EXISTS mergedTableHorizontal;')
        cur.execute('CREATE TABLE mergedTableHorizontal AS (SELECT * FROM horizontal.cheap_comedy UNION SELECT * FROM horizontal.cheap_comedy_rest);')
        cur.execute('SELECT count(*) FROM mergedTableHorizontal;')
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