from flask import Flask, jsonify, render_template, request, redirect, url_for

from models import User, Confession, Comment, Like

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

@app.route("/spill")
def spill():
    return render_template("spill.html")

@app.route("/spill/successful")
def spilt():
    return render_template("spilt.html")

@app.route("/spill/new", methods=["POST"])
def new_confession():
    new_confession_text = request.form["confession"]
    allow_comments = request.form["allow_comments"]
    new_id = len(confessions_datastore) + 1
    user_id = 1
    new_confession = Confession(new_id, user_id, new_confession_text, allow_comments)
    confessions_datastore.append(new_confession)
    return redirect(url_for("spilt"))

@app.route("/spill/view/<int:id>")
def spill_view(id):
    confession = confessions_datastore[id]
    return render_template("individual_spill.html", confession=confession)

@app.route("/comment/new/<int:id>", methods=["POST"])
def new_comment(id):
    confession = confessions_datastore[id]
    if not confession.allow_comments:
        return redirect(url_for("error_page"))
    new_comment_text = request.form["comment"]
    user_id = 1
    new_comment = Comment(user_id, new_comment_text)
    confession.add_comment(new_comment)
    return redirect(url_for("spill_view", id=id))

@app.route("/error")
def error_page():
    return render_template("error.html")

@app.route("/random")
def random():
    return render_template("random.html")

@app.route("/about")
def about():
    return render_template("about.html")






if __name__ == '__main__':
    app.run(debug=True, port=8080)