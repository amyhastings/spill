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

@app.route("/spill/<int:confession_id>")
def spill_view(confession_id):
    confession = confessions_datastore[confession_id]
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
    if "allow_comments" in request.form:
        allow_comments = request.form["allow_comments"]
    else:
        allow_comments = False
    new_confession_id = len(confessions_datastore)
    user_id = session['user_id']
    new_confession = Confession(new_confession_id, user_id, new_confession_text, allow_comments)
    confessions_datastore.append(new_confession)
    return redirect(url_for("spilt"))

@app.route("/spill/<int:confession_id>/delete", methods=["POST"])
def delete_confession(confession_id):
    confession = confessions_datastore[confession_id]
    user_id = session['user_id']
    if confession.confession_created_by(user_id):
        confessions_datastore.remove(confession)
    else:
        return redirect(url_for("error_page"))
    return redirect(url_for("confirm_confession_deleted"))

@app.route("/spill/delete_confirmed")
def confirm_confession_deleted():
    return render_template("delete_confirmed.html")

@app.route("/spill/<int:confession_id>/comment/new", methods=["POST"])
def new_comment(confession_id):
    confession = confessions_datastore[confession_id]
    if not confession.allow_comments:
        return redirect(url_for("error_page"))
    new_comment_text = request.form["comment"]
    user_id = session['user_id']
    new_comment = Comment(user_id, new_comment_text)
    confession.add_comment(new_comment)
    print("user adding comment:" + str(user_id))
    return redirect(url_for("spill_view", confession_id=confession_id))

@app.route("/spill/<int:confession_id>/comment/<int:comment_id>/delete", methods=["POST"])
def delete_comment(confession_id, comment_id):
    confession = confessions_datastore[confession_id]
    user_id = session['user_id']
    comment = confession.get_comment(comment_id)
    if comment.comment_created_by(user_id):
        confession.delete_comment(comment)
    return redirect(url_for("spill_view", confession_id=confession_id))


@app.route("/spill/<int:confession_id>/like")
def new_like(confession_id):
    confession = confessions_datastore[confession_id]
    user_id = session['user_id']
    confession.add_like(user_id)
    return ""

@app.route("/spill/<int:confession_id>/unlike")
def remove_like(confession_id):
    confession = confessions_datastore[confession_id]
    user_id = session['user_id']
    confession.remove_like(user_id)
    return ""

@app.route("/spill/<int:confession_id>/likes_count")
def likes_count(confession_id):
    likes_count = confessions_datastore[confession_id].get_likes_count()
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