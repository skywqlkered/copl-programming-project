from Shoppinglist import Shoppinglist
from RecipeBook import RecipeBook

class User:
    def __init__(self, name):
        """
        Initializes a User object.

        Args:
            name (str): The name of the user.
            
        Attributes:
            name (str): The name of the user.
            _shoppinglists (list): A private list of shopping lists associated with the user.
            __recipebooks (list): A private list of recipe books associated with the user.
        """

        self.name = name
        self._shoppinglists = []
        self.__recipebooks = []

    def add_shoppinglist(self, shoppinglist: Shoppinglist):
        """
        Adds a shoppinglist to the user's collection of shoppinglists.

        Args:
            shoppinglist (Shoppinglist): The shoppinglist to add.
        """
        if shoppinglist not in self._shoppinglists:
            self._shoppinglists.append(shoppinglist)

    def add_recipebook(self, recipebook: RecipeBook):
        """
        Adds a recipebook to the user's collection of recipebooks.

        Args:
            recipebook (RecipeBook): The recipebook to add.
        """
        if recipebook not in self._recipebooks:
            self._recipebooks.append(recipebook)


    def rem_shoppinglist(self, shoppinglist: Shoppinglist):
        """
        Removes a shopping list from the user's collection of shopping lists.

        Args:
            shoppinglist (Shoppinglist): The shopping list to remove.
        """

        if shoppinglist in self._shoppinglists:
            self._shoppinglists.remove(shoppinglist)

    def rem_recipebook(self, recipebook: RecipeBook):
        """
        Removes a recipebook from the user's collection of recipebooks.

        Args:
            recipebook (RecipeBook): The recipebook to remove.
        """
        if recipebook in self._recipebooks:
            self._recipebooks.remove(recipebook)

    @property
    def shoppinglists(self):
        """
        Returns a list of all shopping lists associated with the user.
        """

        return self._shoppinglists

    @property
    def recipebooks(self):
        """
        Returns a list of all recipebooks associated with the user.
        """
        
        return self.__recipebooks
    
    