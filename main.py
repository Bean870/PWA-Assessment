from flask import Flask, render_template, request
import db

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)

##################################
### New code starts here
##################################
@app.route("/login", methods=["GET", "POST"])
def Login():
    return render_template("login.html")
##################################
### New code ends here
##################################

app.run(debug=True, port=5000)
