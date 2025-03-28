from Ingredient import Ingredient


class Shoppinglist:
    def __init__(self):
        """
        Initializes an empty shopping list.

        The shopping list is a dictionary where the keys are Ingredient objects and the values are the amount of that ingredient.
        """
        self.ingredients: dict[str, tuple[list, int]] = {}

    def add_ingredient(self, ingredient: Ingredient, amount: int):
        """
        Adds an ingredient to the shopping list.

        Args:
            ingredient (Ingredient): The ingredient to add.
            amount (int): The amount of the ingredient to add.

        Raises:
            ValueError: If the amount is 0 or less.
        """
        
        if amount <= 0:
            raise ValueError("Cannot add 0 or less of an item")
        if ingredient.name in self.ingredients:
            existing = self.ingredients[ingredient.name]
            existing_amount = existing[1]
            new_amount = existing_amount + amount
            self.ingredients[ingredient.name] = ([ingredient.temperature,
                                                ingredient.expiration_date,
                                                ingredient.quantity],
                                                new_amount)
        else:
            self.ingredients[ingredient.name] = ([ingredient.temperature, 
                                                ingredient.expiration_date, 
                                                ingredient.quantity], 
                                                amount)

    def _handle_remove(self, name: str):
        """
        Handles the removal of an ingredient from the shopping list.

        Args:
            name (str): Name of the ingredient to remove.

        Raises:
            KeyError: If the ingredient is not found in the shoppinglist.
        """
        try:
            del self.ingredients[name]

        except KeyError:
            raise KeyError("Ingredient was not found on the shoppinglist")

    def rem_ingredient(self, name: str, amount: int = None):
        """
        Removes an ingredient from the shopping list.

        Args:
            name (str): Name of the ingredient to remove.
            amount (int, optional): The amount of the ingredient to remove. Defaults to None.

        Raises:
            KeyError: If the ingredient is not found in the shoppinglist.
        """
        if amount:
            existing = self.ingredients[name]
            existing_amount = existing[1]
            new_amount = existing_amount - amount
            self.ingredients[name] = ([existing.temperature,
                                                existing.expiration_date,
                                                existing.quantity],
                                                new_amount)
            if new_amount <= 0:
                self._handle_remove(name)

        else:
            self._handle_remove(name)

    def __str__(self):
        """
        Returns a string representation of the shopping list.

        Returns:
            str: A string listing all the ingredients and their respective quantities.
        """
        return_str = ""
        if len(self.ingredients) == 0:
            return "Wow, such empty"
        for i in range(len(self.ingredients)):
            return_str += f"{list(self.ingredients.keys())[i]}: {list(self.ingredients.values())[0][1]}, "
        return f"Shoppinglist: {return_str}"
    

    def __repr__(self):

        """
        Returns a list of ingredient names in the shopping list.

        Returns:
            list: A list of ingredient names.
        """

        return str([ingredient for ingredient in self.ingredients.keys()])

    def __add__(self, another: 'Shoppinglist'):
        """
        Adds two shopping lists together.

        Args:
            another (Shoppinglist): The other shopping list to add.

        Returns:
            dict: A dictionary of ingredients and their respective quantities
        """
        added = self.ingredients.copy()
        for i in another.ingredients:
            if i not in added:
                added[i] = another.ingredients[i]
            else:
                existing = added[i]
                added[i] = existing[0], existing[1] + another.ingredients[i][1]
        return added

    def __sub__(self, another: 'Shoppinglist'):
        """
        Subtracts the ingredients in another shopping list from this one.

        Args:
            another (Shoppinglist): The other shopping list to subtract.

        Returns:
            dict: A dictionary of ingredients and their respective quantities
        """
        added: dict = self.ingredients.copy()
        for i in another.ingredients:
            if i in added:
                existing = added[i]
                added[i] = existing[0], existing[1] - another.ingredients[i][1]
                
                if added[i][1] <= 0:
                    del added[i]
        return added

    def __mul__(self, multipier):
        """
        Multiply all amounts of ingredients in the shopping list by a certain number

        Args:
            multipier (int): The number to multiply by

        Raises:
            ValueError: If the multipier is not an integer or is less than or equal to 0

        Returns:
            dict: A new shopping list with all amounts multiplied
        """
        if not isinstance(multipier, int):
            raise ValueError("Can only multiply by integers")
        if multipier <= 0:
            raise ValueError("Can not multiply by 0 or less")
        mult: dict = self.ingredients.copy()
        for i in mult:
            mult[i] *= multipier
        return mult

    def __rmul__(self, multipier):
        """see __mul__"""
        return self.__mul__(multipier)

