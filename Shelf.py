from Ingredient import Ingredient
from datetime import datetime

class Shelf():
    """A shelf in which ingredients can be stored.
    Has a storage space."""
    def __init__(self, storage_space):
        """Sets up a shelf object. Arg: storage_space (int) - Amount of storage the shelf has."""
        self.storage_space = storage_space
        self._ingredients: list[str, int, datetime, int] = []

    def in_shelf(self, check_ingredient: Ingredient):
        """Checks if a certain ingredient is already in the shelf."""
        for ingredient in self._ingredients:
            if ingredient == check_ingredient:
                return True
        return False

    def storable(self, ingredient: Ingredient):
        """Checks if there is enough space on the shelf for an ingredient."""
        if ingredient.quantity <= self.storage_space:
            return True
        else:
            return False

    def add_ingredient(self, new_ingredient: Ingredient):
        """Adds an ingredient to the shelf. Raises a ValueError if there is not enough space."""
        if self.storable(new_ingredient):
            for ingredient in self._ingredients:
                if ingredient == new_ingredient:
                    ingredient.add(new_ingredient.quantity)
                    self.storage_space -= new_ingredient.quantity
                    return None
            self._ingredients.append(new_ingredient)
            self.storage_space -= new_ingredient.quantity
        else:
            raise ValueError("Not enough space in shelf.")

    def remove_ingredient(self, ingredient: Ingredient):
        """Removes an ingredient from the shelf. 
        Raises a ValueError if the ingredient isn't on the shelf.
        Also raise a ValueError if the specified amount of ingredient isn't in the shelf."""
        for item in self._ingredients:
            if item == ingredient:
                if ingredient <= item:
                    amount = item.quantity - ingredient.quantity 
                    self.storage_space += ingredient.quantity
                    if amount == 0:
                        self._ingredients.remove(item)
                        return None
                    item.quantity = amount 
                else:
                    raise ValueError("There is not this amount of ingredient in the shelf.")
                return None
        raise ValueError("Ingredient not in shelf.")
    
    def bad_ingredients(self):
        """Checks if any ingredients in shelve have gone bad.
        Returns:
            expired_ingredients (list of ingredients) - Ingredients that have expired.
            refrigerator_ingredients (list of ingredients) - Ingredients that should have been kept in a refrigerator
        """
        expired_ingredients = []
        refrigerator_ingredients = []
        today = datetime.today()
        for ingredient in self._ingredients:
            if ingredient.expiration_date < today:
                expired_ingredients.append(ingredient)
            elif ingredient.temperature <= 8:
                refrigerator_ingredients.append(ingredient)
        return expired_ingredients, refrigerator_ingredients

    def __str__(self):
        str_ingredients = []
        for item in self._ingredients:
            str_ingredients.append(str(item))
        return f"Shelf has {self.storage_space} space left and contains: {str_ingredients}"
    
    def __repr__(self):
        return f"Shelf({self.storage_space})"