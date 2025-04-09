
from .Post import Post
from .Feed import Feed
from datetime import datetime


class User: 
    """
    Class representing a user in the exo_heritage system.
    """
    
    def __init__(self, username: str, password: str):
        """
        Initialize a User instance.

        :param username: The username of the user.
        :param password: The password of the user.
        """
        self.username = username
        self.password = password
        self.is_connected = False

    def __repr__(self):
        return f"User(username={self.username})"
    
    def se_connecter(self, username: str, password: str):
        """
        Simulate user login.
        """
        if username != self.username or password != self.password:
            print(f"Failed to log in user {username}.")
            raise ValueError("Invalid username or password.")
        else:
            print(f"User {self.username} logged in.")
            self.is_connected = True
    
    def se_deconnecter(self):
        """
        Simulate user logout.
        """
        self.is_connected = False
        print(f"User {self.username} logged out.")
    
    def est_connecte(self) -> bool:
        """
        Check if the user is connected.

        :return: True if the user is connected, False otherwise.
        """
        return self.is_connected

    def inscription(username: str, password: str):
        """
        Simulate user registration.
        """
        # In a real application, you would save the user data to a database.
        User(username, password)
        print("User registered successfully.")

    def creer_un_feed(self, nom_feed: str):
        """
        Simulate creating a feed.

        :param nom_feed: The name of the feed.
        """
        if not self.est_connecte():
            print("User must be logged in to create a feed.")
            raise ValueError("User must be logged in to create a feed.")
    
        date_heure_feed = datetime.now()

        # In a real application, you would save the feed data to a database.
        print(f"Feed '{nom_feed}' created at {date_heure_feed} successfully.")

        return Feed(nom_feed,[],date_heure_feed)

    def poster_un_message(self, message: str, feed, fichier=None):
        """
        Simulate posting a message to a feed.

        :param message: The message to post.
        :param feed: The feed to post the message to.
        """
        if not self.est_connecte():
            print("User must be logged in to post a message.")
            raise ValueError("User must be logged in to post a message.")
        # Récupérer la date et l'heure actuelles
        date_heure_message = datetime.now()

        # In a real application, you would save the message data to a database.
        print(f"Message posted to feed '{feed.nom_feed}' at {date_heure_message}: {message}")
        if fichier:
            print(f"file : '{fichier}'")

        return Post(message, feed, date_heure_message, fichier)