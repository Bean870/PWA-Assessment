#Adds SQL information to the PWA containing stored information on users and comments

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():

    # Connect to the database and return the connections
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllComments():

    # Connect, query all comments and then return the data
    db = GetDB()
    comments = db.execute("SELECT * FROM Comments").fetchall()
    db.close()
    return True

def AddComments(user_id, date, game, comments):
   
    # Check if any boxes were empty
    if date is None or game is None:
        return False
   
    # Get the DB and add the comment
    db = GetDB()
    db.execute("INSERT INTO Comments(user_id, date, game, comments) VALUES (?, ?, ?, ?)",
               (user_id, date, game, comments,))
    db.commit()

 comments = db.execute("""SELECT Comments.date, Comments.game, Comments.score, Users.username
                            FROM Comments JOIN Users ON Comments.user_id = Users.id
                            ORDER BY date DESC""").fetchall()

    return GetAllComments