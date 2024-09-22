import datetime

class User:
    def __init__(self, user_id):
        self.id = user_id

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

    def get_comment(self, comment_id):
        return self.comments[comment_id]
    
    def delete_comment(self, comment):
        self.comments.remove(comment)
    
    def add_like(self, like):
        self.likes.append(like)

    def print(self):
        print(self.text)
        for comment in self.comments:
            print(comment.text)    
    
    def add_like(self, user_id):
        if not user_id in self.likes:
            self.likes.append(user_id)

    def remove_like(self, user_id):
        self.likes.remove(user_id)

    def get_likes_count(self):
        return len(self.likes)

class Comment:
    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text
        self.timestamp = datetime.datetime.now()
    
    def comment_created_by(self, user_id):
        return self.user_id == user_id
