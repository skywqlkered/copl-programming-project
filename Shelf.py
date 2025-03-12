from Ingredient import Ingredient

class Shelf():
    def __init__(self, storage_space):
        self.__storage_space = storage_space
        self._ingredients = []

    @property
    def storage_space(self):
        return self.__storage_space

    def storable(self, ingredient: Ingredient):
        if ingredient.__quantity <= self.__storage_space:
            return True
        else: 
            return False

    def add_ingredient(self, new_ingredient: Ingredient):
        if self.storable:
            for ingredient in self._ingredients:
                if ingredient == new_ingredient:
                    ingredient.add(new_ingredient.quantity)
                    return None
            self._ingredients.append(new_ingredient)
        else:
            raise ValueError("Not enough space in shelf.")

    def remove_ingredient(self, ingredient: Ingredient):
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
    
    def in_shelf(self, check_ingredient: Ingredient):
        for ingredient in self._ingredients:
            if ingredient == check_ingredient:
                return True
        return False
    
    def __str__(self):
        return f"Shelf has {self.__storage_space} space left and contains: {self._ingredients}"