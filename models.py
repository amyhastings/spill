import datetime

class User:
    def __init__(self, userid):
        self.id = userid

class Confession:
    def __init__(self, id, user_id, text):
        self.id = id
        self.user_id = user_id
        self.text = text
        self.comments = []
        self.votes = []
        self.timestamp = datetime.datetime.now()

    def add_comment(self, comment):
        self.comments.append(comment)

    def print(self):
        print(self.text)
        for comment in self.comments:
            print(comment.text)    
    
    def add_vote(self, upvote):
        self.votes.append(upvote)

    def get_upvote_count(self):
        upvote_count = 0
        for vote in self.votes:
            if vote.upvote:
                upvote_count += 1
        return upvote_count
    
    def get_downvote_count(self):
        downvote_count = 0
        for vote in self.votes:
            if not vote.upvote:
                downvote_count += 1
        return downvote_count



class Comment:
    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text
        self.timestamp = datetime.datetime.now()

class Vote:
    def __init__(self, user_id, upvote):
        self.user_id = user_id
        self.upvote = upvote