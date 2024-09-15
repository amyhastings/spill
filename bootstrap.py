from prebaked_confessions import confessions

from models import Confession, Comment, Like

def bootstrap_confessions():
    confessions_datastore = []
    for confession in confessions:
        new_confession = Confession(confession["id"], confession["user_id"], confession["text"], confession["allow_comments"])
        for comment in confession["comments"]:
            new_comment = Comment(comment["user_id"], comment["text"])
            new_confession.add_comment(new_comment)
        for like in confession["likes"]:
            new_like = Like(like["user_id"])
            new_confession.add_like(new_like)
        confessions_datastore.append(new_confession)
    return confessions_datastore