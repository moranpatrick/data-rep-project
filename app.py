#Flask Imports
from flask import Flask, render_template, g, request, url_for, session, redirect, flash
from functools import wraps
import sqlite3

app = Flask(__name__)
app.database = "data/formData.db"
# Session keys proctects the session being accessed on the clients side
# Ideally you should use a random key generator to generate a secret key and
# store the key in a seperate config file which should be imported to flask for
# security reasons but for this project we will haed code one here.
app.secret_key = "testLogin"

#route to homepage
@app.route('/')
def index():
    #establish connection to database
    g.db = connect_db()
    #execute query
    cur = g.db.execute('select * from teamData')
    posts = [dict(position=row[0], names=row[1]) for row in cur.fetchall()]
    g.db.close()
    # When routed here render home page template
    return render_template("homePage.html", posts = posts)

#route to form page
@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        #request name from form
        nameInput = request.form['nameInput']
        #request mesage from form
        message = request.form['messageInput']
        #establish database connection
        g.db = connect_db()
        #execute sql query
        g.db.execute('INSERT INTO postData values(?,?)', (nameInput, message))
        #commit to database
        g.db.commit()
        #close database connection
        g.db.close()
        #if request is a post redirect to forum
        return redirect(url_for('forum'))
    else:
        #otherwise render form template
        return render_template("form.html")

#route to forum page
@app.route('/forum')
def forum():
    #establish connection to database
    g.db = connect_db()
    #execute query
    cur = g.db.execute('select * from postData')
    #convert into a dictionary so python can understand it
    posts = [dict(name=row[0], message=row[1]) for row in cur.fetchall()]
    #close the datbase connection
    g.db.close()
    # When routed here render forum template, pass through variable to the html template
    return render_template("forum.html", posts=posts)


# Login required fucnction using functools.wrap
#https://docs.python.org/2/library/functools.html?highlight=wraps#functools.wraps
#The intended use for this function is in decorator functions which wrap the decorated function and return the wrapper.
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            #error handling using flash messaging
            flash('You Need To Login First')
            #unsuccessful logins get redirected to the login page
            return redirect(url_for('login'))
    return wrap

@app.route('/teamEntry', methods = ['GET','POST'])
#login required decorator - you must be logged in to view this page
@login_required
def teamEntry():
    if request.method == 'POST':
        #request team position from the form
        position = request.form['positionInput']
        #converts the string to uppercase
        position = position.upper()
        #request player names from the form input
        names = request.form['namesInput']
        #establish connection
        g.db = connect_db()
        #execute query and update the database
        g.db.execute('update teamData set position=?,names=? where position = ?', (position, names, position))
        #commit query
        g.db.commit()
        #close database connection
        g.db.close()
    return render_template("teamEntry.html")

def connect_db():
    #funtion which makes database connection
    return sqlite3.connect(app.database)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            flash('Invalid Credentials - Please Try Again!')
        else:
            # if the users credentials are correct then the value true is assigned to logged in key
            session['logged_in'] = True
            #successfully logged in so redirect to the team entry page
            return redirect(url_for('teamEntry'))
    #render login template if login is unsuccessful
    return render_template("login.html")

@app.route('/logout')
#login required decorator - you must be logged in to view this page
@login_required
def logout():
    #session.pop deletes the key by setting logged_in from true to None
    session.pop('logged_in', None)
    #return to homepage after a logout
    return redirect(url_for('index'))

#Run App
if __name__ == '__main__':
    app.run()