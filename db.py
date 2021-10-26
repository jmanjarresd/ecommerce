import sqlite3

def obtener_conexion():
    return sqlite3.connect('ecommerce.db')

""" from sqlite3 import Error
from flask import current_app, g

def obtener_conexion():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect("ecommerce.db")
            g.db.row_factory = sqlite3.Row
        return g.db
    except Error:
        print( Error )


def close_db():
    db = g.pop( 'db', None )

    if db is not None:
        db.close() """

""" import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='password',
                                db='ecommerce') """
