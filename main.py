#Imports flask to access the PWA

from flask import Flask, render_template, request
import db
#Creates Flask
app = Flask(__name__)
app.secret_key = "gtg"
#Route to the home page
@app.route("/")
def Home():
    commentsData = db.GetAllComments()
    return render_template("index.html", comments=commentsData)

#Adds a login method for users
@app.route("/login", methods=["GET", "POST"])
def Login():
    return render_template("login.html")

#Connects the ratings webpage to the PWA
@app.route("/add", methods=["GET","POST"])
def Add():
 
 # Check if they are logged in first
    if session.get('username') == None:
        return redirect("/")

    # Has it been submitted?
    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        game = request.form['game']
        score = request.form['comment']

        # Sends data to add new comments
        db.AddGuess(user_id, date, game, comment)

    return render_template("add.html")

app.run(debug=True, port=5000)