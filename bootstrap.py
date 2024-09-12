from prebaked_confessions import confessions

from models import Confession, Comment, Vote

def bootstrap_confessions():
    confessions_datastore = []
    for confession in confessions:
        new_confession = Confession(confession["id"], confession["user_id"], confession["text"])
        for comment in confession["comments"]:
            new_comment = Comment(comment["user_id"], comment["text"])
            new_confession.add_comment(new_comment)
        for vote in confession["votes"]:
            new_vote = Vote(vote["user_id"], vote["upvote"])
            new_confession.add_vote(new_vote)
        confessions_datastore.append(new_confession)
    return confessions_datastore