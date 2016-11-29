#Flask Imports
from flask import Flask, render_template, g, request, url_for, session, redirect
import sqlite3

app = Flask(__name__)
app.database = "data/formData.db"
app.secret_key = "testLogin"

@app.route('/')
def index():
    g.db = connect_db()
    cur = g.db.execute('select * from teamData')
    posts = [dict(position=row[0], names=row[1]) for row in cur.fetchall()]
    g.db.close()
    # When routed here render home page template
    return render_template("homePage.html", posts = posts)

@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        nameInput = request.form['nameInput']
        message = request.form['messageInput']
        g.db = connect_db()
        g.db.execute('INSERT INTO postData values(?,?)', (nameInput, message))
        g.db.commit()
        g.db.close()
        #if request is a post redirect to forum
        return redirect(url_for('forum'))
    else:
        #otherwise render form template
        return render_template("form.html")

@app.route('/forum')
def forum():
    #establish connection to database
    g.db = connect_db()
    #execute query
    cur = g.db.execute('select * from postData')
    #convert into a dictionary so python can understand it
    posts = [dict(name=row[0], message=row[1]) for row in cur.fetchall()]
    g.db.close()
    # When routed here render forum template, pass through variable to the html template
    return render_template("forum.html", posts=posts)

@app.route('/teamEntry', methods = ['GET','POST'])
def teamEntry():
    if request.method == 'POST':
        position = request.form['positionInput']
        position = position.upper()
        names = request.form['namesInput']
        g.db = connect_db()
        g.db.execute('update teamData set position=?,names=? where position = ?', (position, names, position))
        g.db.commit()
        g.db.close()
    return render_template("teamEntry.html")

def connect_db():
    return sqlite3.connect(app.database)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Crediantials!! Try Again'
        else:
            session['logged_in'] = True
            return redirect(url_for('teamEntry'))

    return render_template("login.html", error=error)

@app.route('/logout')
def logout():
    #session.pop deletes the key by setting logged_in from true to None
    session.pop('logged_in', None)
    message = 'suceefully logged out'
    #return to homepage after a logout
    return redirect(url_for('index'))


#Run App
if __name__ == '__main__':
    app.run(debug=True)