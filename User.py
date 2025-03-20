from Shoppinglist import Shoppinglist
from RecipeBook import RecipeBook

class User:
    def __init__(self, name):
        self.name = name
        self._shoppinglists = []
        self._recipebooks = []

    def add_shoppinglist(self, shoppinglist: Shoppinglist):
        if shoppinglist not in self._shoppinglists:
            self._shoppinglists.append(shoppinglist)

    def add_recipebook(self, recipebook: RecipeBook):
        self._recipebooks.append(recipebook)



    def rem_shoppinglist(self, shoppinglist: Shoppinglist):
        if shoppinglist in self._shoppinglists:
            self._shoppinglists.remove(shoppinglist)

    def rem_recipebook(self, recipebook: RecipeBook):
        if recipebook in self._recipebooks:
            self._recipebooks.remove(recipebook)

