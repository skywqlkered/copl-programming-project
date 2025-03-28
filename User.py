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
            _recipebook (list[RecipeBook]): The recipe books of the user.
            refrigerator Refrigerator: The refrigerators of the user.
        """

        self.name = name
        self.mealplan: MealPlan = MealPlan()
        self._shoppinglist: Shoppinglist = Shoppinglist()
        self.__recipebook: RecipeBook = RecipeBook()
        self.storage: dict[Refrigerator, Shelf] = {"refrigerator": None, "shelf": None}
        self.__password = None
        self.__birthplace = None

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def birthplace(self):
        return self.__birthplace
    
    @birthplace.setter
    def birthplace(self, birthplace):
        self.__birthplace = birthplace

    def add_recipebook(self, new_recipbebook: RecipeBook):
        """
        Adds a recipebook to the user's collection of recipebooks.

        Args:
            recipebook (RecipeBook): The recipebook to add.
        """
        if self.__recipebook != new_recipbebook:
            self.__recipebook = new_recipbebook


    def rem_recipebook(self, new_recipebook: RecipeBook):
        """
        Removes a recipebook from the user's collection of recipebooks.

        Args:
            recipebook (RecipeBook): The recipebook to remove.
        """
        if self.__recipebook == new_recipebook:
            self.__recipebook = None

    @property
    def recipebook(self):
        """
        Returns a list of all recipebooks associated with the user.
        """
        return self.__recipebook

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
        if self.storage["refrigerator"] != refrigerator:
            self.storage["refrigerator"] = refrigerator

    def rem_refrigerator(self, refrigerator: Refrigerator):
        if self.storage["refrigerator"] == refrigerator:
            self.storage["refrigerator"] = None

    def add_shelf(self, shelf: Shelf):
        """
        Adds a shelf to the user's collection of shelves.

        Args:
            shelf (Shelf): The shelf to add.
        """
        if self.storage["shelf"] != shelf:
            self.storage["shelf"] = shelf
        

    def rem_shelf(self, shelf: Shelf):
        """
        Removes a shelf from the user's collection of shelves.

        Args:
            shelf (Shelf): The shelf to remove.
        """
        if self.storage["shelf"] == shelf:
            self.storage["shelf"] = None


    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: A string representation of the user.
        """
        return f"User: {self.name}"