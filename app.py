from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("homePage.html")

@app.route('/form')
def formPage():
    return render_template("form.html")

@app.route('/forum')
def forum():
    return render_template("forum.html")

if __name__ == '__main__':
    app.run()
