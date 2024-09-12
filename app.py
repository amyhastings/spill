from flask import Flask, jsonify, render_template, request, redirect, url_for

# from models import User, Confession, Comment, Vote

from bootstrap import bootstrap_confessions

app = Flask(__name__)

# Default data:
users_datastore = []
# write a function to store all my users in this datastore
confessions_datastore = bootstrap_confessions()
#write a function that takes the bootstrap data and creates confession objects and puts them in this list
#we want the comments and votes to live here too

@app.route('/')
def home():
    return render_template('home.html', confessions=confessions_datastore)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
