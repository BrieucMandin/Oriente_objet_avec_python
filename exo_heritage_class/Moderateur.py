from datetime import datetime
from .Post import Post
from .Feed import Feed
from .User import User


class Moderator(User):
    """
    Class representing a moderator in the system.
    """

    def __init__(self, username: str, password: str):
        """
        Initialize a Moderator instance.

        :param username: The username of the moderator.
        :param password: The password of the moderator.
        """
        super().__init__(username, password)
        self.is_moderator = True

    def supprimer_post(self, post: Post):
        """
        Delete a post.

        :param post: The post to delete.
        """
        # Logic to delete the post
        post.__del__()
        
    

    def modifier_post(self, post: Post, new_content: str, new_date: str = None, modify_file: bool = False, new_file=None):


        """
        Modify a post.

        :param post: The post to modify.
        :param new_content: The new content of the post.
        """
        # Logic to modify the post

        if modify_file:
            # Logic to modify the file
            post.post_modificator(post, post.title, new_content, new_date, new_file)
        else:
            post.post_modificator(post, post.title, new_content, new_date)



    def delete_feed(self, feed: Feed):
        """
        Delete a feed.
        :param feed: The feed to delete.
        """
        # Logic to delete the feed
        feed.__del__()
        # In a real application, you would remove the feed from the database or storage.
        # For now, we just print a message.
        print(f"Feed {feed.name} deleted.")

    def modify_feed(self, feed: Feed, new_name: str, removes_items = None, items = None):
        """
        Modify a feed.

        :param feed: The feed to modify.
        :param new_name: The new name of the feed.
        """
        # Logic to modify the feed
        if new_name:
            feed.modify(new_name)
        if items is not None:
            feed.modify(new_name, items)
        if removes_items is not None:
            feed.modify(new_name, remove_items=removes_items)
        

