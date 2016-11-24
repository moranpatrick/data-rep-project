#Couchdb import
import couchdb
couch = couchdb.Server("http://localhost:5984")

db = couch['forum']

#Flask Imports
from flask import Flask, render_template

app = Flask(__name__)

#save function
def save_post(db, post):
    post['_email'] = post['id_postStr']
    db.save(post)

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
    # When routed here render forum template
    return render_template("forum.html")

#Run App
if __name__ == '__main__':
    app.run(debug=True)