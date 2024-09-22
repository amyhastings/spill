from flask import Flask, jsonify, render_template, request, redirect, url_for, session

from models import User, Confession, Comment

from bootstrap import bootstrap_confessions, bootstrap_users

app = Flask(__name__)
app.secret_key = '1gdxJCSYMHFlwP0JIEokQA'

# Default data:
users_datastore = bootstrap_users()
# write a function to store all my users in this datastore
confessions_datastore = bootstrap_confessions()
#write a function that takes the bootstrap data and creates confession objects and puts them in this list
#we want the comments and votes to live here too

@app.before_request
def identify_user():
    if not 'user_id' in session.keys():
        new_user_id = len(users_datastore) + 1
        users_datastore.append(User(new_user_id))
        session['user_id'] = new_user_id
        print("adding user:" + str(new_user_id))
    else:
        print("current user:" + str(session['user_id']))


@app.route('/')
def home():
    return render_template('home.html', confessions=confessions_datastore)

@app.route("/spill/<int:id>")
def spill_view(id):
    confession = confessions_datastore[id]
    return render_template("individual_spill.html", confession=confession)

# Displays new confession form
@app.route("/spill")
def spill():
    return render_template("spill.html")

# Displays text showing confession submission was successful
@app.route("/spill/successful")
def spilt():
    return render_template("spilt.html")

# Accepts new confession form submission - redirects to spilt.html showing confession submission was successful
@app.route("/spill/new", methods=["POST"])
def new_confession():
    new_confession_text = request.form["confession"]
    allow_comments = request.form["allow_comments"]
    new_id = len(confessions_datastore) + 1
    user_id = 1
    new_confession = Confession(new_id, user_id, new_confession_text, allow_comments)
    confessions_datastore.append(new_confession)
    return redirect(url_for("spilt"))


@app.route("/spill/<int:id>/comment/new", methods=["POST"])
def new_comment(id):
    confession = confessions_datastore[id]
    if not confession.allow_comments:
        return redirect(url_for("error_page"))
    new_comment_text = request.form["comment"]
    user_id = session['user_id']
    new_comment = Comment(user_id, new_comment_text)
    confession.add_comment(new_comment)
    print("user adding comment:" + str(user_id))
    return redirect(url_for("spill_view", id=id))

@app.route("/spill/<int:id>/like")
def new_like(id):
    confession = confessions_datastore[id]
    user_id = session['user_id']
    confession.add_like(user_id)
    return ""

@app.route("/spill/<int:id>/unlike")
def remove_like(id):
    confession = confessions_datastore[id]
    user_id = session['user_id']
    confession.remove_like(user_id)
    return ""

@app.route("/spill/<int:id>/likes_count")
def likes_count(id):
    likes_count = confessions_datastore[id].get_likes_count()
    return { "likes_count" : likes_count }

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