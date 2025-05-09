from .Feed import Feed
from datetime import datetime

class Post:
    def __init__(self, title: str, content: str,feed: Feed ,date: datetime = None, fichier=None):
        self.title = title
        self.content = content
        self.date = date
        self.fichier = fichier
        
        feed.AddPost(self)  # Add the post to the feed's list of posts


    def __str__(self):
        return f"Post(contenu={self.content}, feed={self.title}, date_heure={self.date}, fichier={self.fichier})"
    
    def post_modificator(self, post,title: str = None, content: str = None, date: str = None, fichier=None):
        """
        Modifies the current post with the attributes of another post.
        """
        self.title = post.title
        self.content = post.content
        self.date = post.date
        self.fichier = post.fichier
        print(f"Post {self.title} modified with new content: {self.content}, date: {self.date}, file: {self.fichier}")
    
    def __del__(self):
        """
        Destructor to clean up resources.
        """
        print(f"Post {self.title} deleted.")