from Shoppinglist import Shoppinglist
from RecipeBook import RecipeBook
from Refrigerator import Refrigerator
from MealPlan import MealPlan
from Shelf import Shelf

class User:
    def __init__(self, name):
        """
        Initializes a User object with a name and optional attributes for meal planning, shopping lists, recipe books, and refrigerators.

        Args:
            name (str): The name of the user.
        Attributes:
            mealplan (MealPlan): The meal plan of the user.
            _shoppinglist (Shoppinglist): The shopping list of the user.
            _recipebooks (list[RecipeBook]): The recipe books of the user.
            refrigerator Refrigerator: The refrigerators of the user.
        """

        self.name = name
        self.mealplan: MealPlan = MealPlan()
        self._shoppinglist: Shoppinglist = Shoppinglist()
        self.__recipebooks: list[RecipeBook] = []
        self.storage: dict[list[Refrigerator], list[Shelf]] = {"refrigerators": [], "shelves": []}

        self.add_recipebook(RecipeBook()) # the default recipe book to save misc recipes

    def add_recipebook(self, recipebook: RecipeBook):
        """
        Adds a recipebook to the user's collection of recipebooks.

        Args:
            recipebook (RecipeBook): The recipebook to add.
        """
        if recipebook not in self.__recipebooks:
            self.__recipebooks.append(recipebook)


    def rem_recipebook(self, recipebook: RecipeBook):
        """
        Removes a recipebook from the user's collection of recipebooks.

        Args:
            recipebook (RecipeBook): The recipebook to remove.
        """
        if recipebook in self._recipebooks:
            self._recipebooks.remove(recipebook)

    @property
    def recipebooks(self):
        """
        Returns a list of all recipebooks associated with the user.
        """
        return self.__recipebooks

    def has_item(self, item_name: str = None):
        """
        Finds an item in refrigerator or shelf.

        Args:
            item_name (str): The name of the item to find.

        Returns:
            item: Ingredient: if the item is found.
        """
        if item_name:
            for storage_type, value in self.storage.items():
                for frige in value:
                    for ing in frige._ingredients:
                        if ing.name == item_name:
                            return [ing]
            else:
                return None
        else:
            all_items = []
            for storage_type in self.storage.keys():
                for shelf in self.storage[storage_type]:
                    all_items.append(shelf._ingredients)
            return all_items

                

        
    def add_refrigerator(self, refrigerator: Refrigerator):
        """
        Adds a refrigerator to the user's collection of refrigerators.

        Args:
            refrigerator (Refrigerator): The refrigerator to add.
        """
        if refrigerator not in self.storage["refrigerators"]:
            self.storage["refrigerators"].append(refrigerator)

    def rem_refrigerator(self, refrigerator: Refrigerator):
        """
        Removes a refrigerator from the user's collection of refrigerators.

        Args:
            refrigerator (Refrigerator): The refrigerator to remove.
        """
        if refrigerator in self.storage["refrigerators"]:
            self.storage["refrigerators"].remove(refrigerator)

    def add_shelf(self, shelf: Shelf):
        """
        Adds a shelf to the user's collection of shelves.

        Args:
            shelf (Shelf): The shelf to add.
        """
        if shelf not in self.storage["shelves"]:
            self.storage["shelves"].append(shelf)
        

    def rem_shelf(self, shelf: Shelf):
        """
        Removes a shelf from the user's collection of shelves.

        Args:
            shelf (Shelf): The shelf to remove.
        """
        if shelf in self.storage["shelves"]:
            self.storage["shelves"].remove(shelf)

