

class Feed:
    """
    Feed class to represent a feed with a name and a list of items.
    """

    def __init__(self, name: str, Posts: list, date: str = None):
        """
        Initialize the Feed with a name and a list of items.

        :param name: The name of the feed.
        :param items: The list of items in the feed.
        """
        self.name = name
        self.Posts = Posts
        self.date = date


    
    def __repr__(self):
        posts_repr = [repr(post) for post in self.Posts]  # Utilise __repr__ de Post pour chaque élément
        return f"Feed(name={self.name}, items={posts_repr}, date={self.date})"

    def modify(self, name: str = None, items: list = None, remove_items: list = None):
        """
        Modify the feed's name and/or items.

        :param name: The new name of the feed.
        :param items: The new list of items in the feed.
        """
        if name:
            self.name = name  # Remplacer le nom (si souhaité)

        if items is not None:  
            self.items = items  # Remplacer toute la liste (si souhaité)

        if remove_items is not None:
            # Supprimer les éléments demandés
            self.items = [item for item in self.items if item not in remove_items]  

        print(f"Feed modified: {self.name} with items {self.items}")

    def __del__(self):
        """
        Destructor for the Feed class.
        """
        print(f"Feed {self.name} is being deleted.")