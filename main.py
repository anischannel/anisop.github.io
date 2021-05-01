from flask import Flask, render_template

from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()




app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/more")
def more():
    return render_template('more.html')

app.run(debug=True)
