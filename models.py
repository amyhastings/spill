import datetime

class User:
    def __init__(self, userid):
        self.id = userid

class Confession:
    def __init__(self, id, user_id, text, allow_comments):
        self.id = id
        self.user_id = user_id
        self.text = text
        self.allow_comments = allow_comments
        self.comments = []
        self.likes = []
        self.timestamp = datetime.datetime.now()

    def add_comment(self, comment):
        self.comments.append(comment)

    def print(self):
        print(self.text)
        for comment in self.comments:
            print(comment.text)    
    
    def add_like(self, user_id):
        new_like = Like(user_id)
        self.likes.append(new_like)

    def get_likes_count(self):
        return len(self.likes)


class Comment:
    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text
        self.timestamp = datetime.datetime.now()

class Like:
    def __init__(self, user_id):
        self.user_id = user_id