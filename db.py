import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllComments():

    # Connect, query all comments and then return the data
    db = GetDB()
    comments = db.execute("SELECT * FROM Comments").fetchall()
    db.close()
    return comments
