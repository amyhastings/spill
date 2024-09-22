from prebaked_confessions import confessions, prebaked_user_count

from models import Confession, Comment, User

def bootstrap_confessions():
    confessions_datastore = []
    for confession in confessions:
        new_confession = Confession(confession["id"], confession["user_id"], confession["text"], confession["allow_comments"])
        for comment in confession["comments"]:
            new_comment = Comment(comment["user_id"], comment["text"])
            new_confession.add_comment(new_comment)
        for user_id in confession["likes"]:
            new_confession.add_like(user_id)
        confessions_datastore.append(new_confession)
    return confessions_datastore

def bootstrap_users():
    users_datastore = []
    for u in range(prebaked_user_count):
        users_datastore.append(User(u))
    print([u.id for u in users_datastore])
    return users_datastore
