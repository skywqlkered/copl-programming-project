from Ingredient import Ingredient


class Shoppinglist:
    def __init__(self):
        """
        Initializes an empty shopping list.

        The shopping list is a dictionary where the keys are Ingredient objects and the values are the amount of that ingredient.
        """
        self.ingredients: dict[Ingredient, int] = {}

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
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += amount
        else:
            self.ingredients[ingredient] = amount

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
            self.ingredients[name] -= amount
            if self.ingredients[name] <= 0:
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
            return_str += f"{list(self.ingredients.keys())[i].name}: {list(self.ingredients.values())[i]}, "
        return f"Shoppinglist: {return_str}"

    def __repr__(self):

        """
        Returns a list of ingredient names in the shopping list.

        Returns:
            list: A list of ingredient names.
        """

        return [ingredient.name for ingredient in self.ingredients]

    def __add__(self, another):
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
                added[i] += another.ingredients[i]
        return added

    def __sub__(self, another):
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
                added[i] -= another.ingredients[i]
                if added[i] <= 0:
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
