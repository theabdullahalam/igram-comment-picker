class Owner:
    def __init__(self, username):
        self.username = username

class Comment:
    def __init__(self, comment_text, username):
        self.text = comment_text
        self.owner = Owner(username)