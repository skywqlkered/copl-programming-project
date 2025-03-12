from Shelf import Shelf
from Ingredient import Ingredient
from datetime import date

class Refrigerator(Shelf):
    def __init__(self, storage_space: int):
        """Sets up a refrigerator object which inherits the shelf object. Arg: storage_space(int) - amount of storage."""
        super().__init__(storage_space)
        self.__temperature = 4
    
    @property
    def temperature(self):
        "Gets the temperature of the refrigerator."
        return self.__temperature
    
    @temperature.setter
    def temperature(self, temperature: int):
        "Sets the temperature of the refrigerator."
        if temperature < 0:
            raise ValueError("Refrigerator should be at least 0 degrees Celcius.")
        elif temperature > 8:
            raise ValueError("Refrigerator should at max be 8 degrees Celcius.")
        else:
            self.__temperature = temperature

    def storable(self, ingredient: Ingredient):
        """Checks if there is enough space on the shelf for an ingredient. And if the temperature is right."""
        if ingredient.__quantity <= self.__storage_space:
            if ingredient.temperature >= self.__temperature-3 or ingredient.temperature <= self.temperature+3:
                return True
            else:
                return False
        else:
            return False
    
    def bad_ingredients(self):
        """Checks if any ingredients in refrigerator have expired."""
        bad_ingredients = []
        today = date.today()
        for ingredient in bad_ingredients:
            if ingredient.expiration_date < today:
                bad_ingredients.append(ingredient)
        return bad_ingredients
    