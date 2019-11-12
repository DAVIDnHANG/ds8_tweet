from flask import Flask, render_template

#make application
app = Flask(__name__)

#make route
@app.route("/")

#now we define a functions
def hello():
    return render_template('home')

#creating another route
@app.route("/about")

def preds():
    return render_template('about')