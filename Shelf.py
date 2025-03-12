from Ingredient import Ingredient


class Shelf():
    def __init__(self):
        self._ingredients = []

    def in_shelf(self, check_ingredient: Ingredient):
        # rewrite this to if ingredient in self._ingredients: return true because reasons
        for ingredient in self._ingredients:
            if ingredient == check_ingredient:
                return True
        return False

    def add_ingredient(self, new_ingredient: Ingredient):
        # this is all wrong and doesnt make sense
        for ingredient in self._ingredients:
            if ingredient == new_ingredient:
                ingredient.add(new_ingredient.quantity)
                return None
        self._ingredients.append(new_ingredient)

    def remove_ingredient(self, ingredient: Ingredient):
        # same thing as above if i in list: is way easier
        for item in self._ingredients:
            if item == ingredient:
                raise NotImplementedError

    def __str__(self):
        ingredients = []
        for ingredient in self._ingredients:
            ingredients.append(str(ingredient))
        return f"{ingredients}"
