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
        """Checks if there is enough space on the refrigerator for an ingredient. And if the temperature is right."""
        if ingredient.quantity <= self.storage_space:
            if ingredient.temperature >= self.__temperature-3 and ingredient.temperature <= self.__temperature+3:
                return True
            else:
                return False
        else:
            return False
        
    def add_ingredient(self, new_ingredient: Ingredient):
        """Adds an ingredient to the refrigerator. Raises a ValueError if there is not enough space 
        or if the ingredient shouldn't be kept in the refrigerator."""
        if self.storable(new_ingredient):
            for ingredient in self._ingredients:
                if ingredient == new_ingredient:
                    ingredient.add(new_ingredient.quantity)
                    self.storage_space -= new_ingredient.quantity
                    return None
            self._ingredients.append(new_ingredient)
            self.storage_space -= new_ingredient.quantity
        else:
            raise ValueError("Not enough space in refrigerator or not right temperature.")
    
    def bad_ingredients(self):
        """Checks if any ingredients in refrigerator have expired."""
        bad_ingredients = []
        today = date.today()
        for ingredient in self._ingredients:
            if ingredient.expiration_date < today:
                bad_ingredients.append(ingredient)
        return bad_ingredients

    

    def __str__(self):
        str_ingredients = []
        for item in self._ingredients:
            str_ingredients.append(str(item))
        return f"Refrigerator has {self.storage_space} space left and contains: {str_ingredients}"