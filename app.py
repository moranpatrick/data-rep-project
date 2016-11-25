

#Flask Imports
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
app.database = "formData.db"


@app.route('/')
def index():
    # When routed here render home page template
    return render_template("homePage.html")

@app.route('/form')
def form():
    #When routed here render from template
    return render_template("form.html")

@app.route('/forum')
def forum():
    g.db = connect_db()
    cur = g.db.execute('select * from postData')
    posts = [dict(name=row[0], message=row[1]) for row in cur.fetchall()]
    g.db.close()
    # When routed here render forum template
    return render_template("forum.html", posts=posts)

def connect_db():
    return sqlite3.connect(app.database)


#Run App
if __name__ == '__main__':
    app.run(debug=True)