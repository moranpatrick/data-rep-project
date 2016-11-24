#Flask Imports
from flask import Flask, render_template

app = Flask(__name__)

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