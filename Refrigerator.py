from Ingredient import Ingredient

class Refrigerator():
    def __init__(self):
        self._ingredients = []

    def in_refrigerator(self, check_ingredient: Ingredient):
        for ingredient in self._ingredients:
            if ingredient == check_ingredient:
                return True
        return False

    def add_ingredient(self, new_ingredient: Ingredient):
        for ingredient in self._ingredients:
            if ingredient == new_ingredient:
                ingredient.quantity += new_ingredient.quantity
                return None
        self._ingredients.append(new_ingredient)

    def __str__(self):
        ingredients = []
        for ingredient in self._ingredients:
            ingredients.append(str(ingredient))
        return f"{self.name} contains {ingredients}"