from Ingredient import Ingredient

class Shelf():
    """A shelf in which ingredients can be stored.
    Has a storage space."""
    def __init__(self, storage_space):
        """Sets up a shelf object. Arg: storage_space (int) - Amount of storage the shelf has."""
        self.__storage_space = storage_space
        self._ingredients = []

    def in_shelf(self, check_ingredient: Ingredient):
        """Checks if a certain ingredient is already in the shelf."""
        for ingredient in self._ingredients:
            if ingredient == check_ingredient:
                return True
        return False

    def storable(self, ingredient: Ingredient):
        """Checks if there is enough space on the shelf for an ingredient."""
        if ingredient.__quantity <= self.__storage_space:
            return True
        else:
            return False

    def add_ingredient(self, new_ingredient: Ingredient):
        """Adds an ingredient to the shelf. Raises a ValueError if there is not enough space."""
        if self.storable:
            for ingredient in self._ingredients:
                if ingredient == new_ingredient:
                    ingredient.add(new_ingredient.quantity)
                    return None
            self._ingredients.append(new_ingredient)
        else:
            raise ValueError("Not enough space in shelf.")

    def remove_ingredient(self, ingredient: Ingredient):
        """Removes an ingredient from the shelf. 
        Raises a ValueError if the ingredient isn't on the shelf.
        Also raise a ValueError if the specified amount of ingredient isn't in the shelf."""
        for item in self._ingredients:
            if item == ingredient:
                if ingredient <= item:
                    item.remove(ingredient.quantity)
                    if item.__quantity == 0:
                        self._ingredients.pop(item)
                else:
                    raise ValueError("There is not this amount of ingredient in the shelf.")
                return None
        raise ValueError("Ingredient not in shelf.")
    
    def __str__(self):
        return f"Shelf has {self.__storage_space} space left and contains: {self._ingredients}"