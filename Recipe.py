from Ingredient import Ingredient

class Recipe:
    """
    A recipe for a dish.
    Includes a name, cooking time, a list of ingredients, and a list of instructions.
    """
    def __init__(self, name: str, cooking_time: int = None):
        """
        Initializes a Recipe object.

        Args:
            name (str): The name of the recipe.
            cooking_time (int) (optional): The time it takes to cook the recipe in minutes.
        """

        if isinstance(cooking_time, int) or isinstance(cooking_time, type(None)):
            self.__cooking_time = cooking_time
        else:
            raise ValueError(f"Cooking time must be an integer or None. (currently {type(cooking_time)}: {cooking_time})")
        
        self.name = name
        self.__ingredients = {}
        self.__instructions = []

    @property
    def ingredients(self):
        """Returns the list of ingredients needed for the recipe."""
        return self.__ingredients
    
    @property
    def instructions(self):
        """Returns the list of instructions to cook the recipe."""
        return self.__instructions
    
    @property
    def cooking_time(self):
        """Returns the time it takes to cook the recipe in minutes. (None if not specified)"""

        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, time: int):
        """
        Sets the time it takes to cook the recipe in minutes.
        Raises a ValueError if the input is not an integer.
        """
        if isinstance(time, int):
            self.__cooking_time = time
        else:
            raise ValueError(f"Cooking time must be an integer. (currently {type(time)}: {time})")

    def add_ingredient(self, ingredient: Ingredient, quantity: int | float):
        """
        Adds an ingredient to the recipe.
        Does nothing if the inputs are invalid.

        Args:
            ingredient (Ingredient): An ingredient.
            quantity (int | float): The amount of the ingredient needed for the recipe.
        """
        try:
            if not isinstance(quantity, int) and not isinstance(quantity, float):
                raise ValueError(f"Quantity must be an integer or a float. (currently {type(quantity)}: {quantity})")
            if ingredient.name in self.__ingredients:
                self.__ingredients[ingredient.name] += quantity
            else:
                self.__ingredients[ingredient.name] = quantity
        except:
            return

    def add_instruction(self, instruction: str):
        """
        Adds an instruction to the recipe.
        Does nothing if the input is invalid.

        Args:
            instruction (str): A step in the recipe.
        """
        if isinstance(instruction, str):
            self.__instructions.append(instruction)

    def __str__(self):
        """Prints the recipe in a readable format."""
        if self.__cooking_time is None:
            time_str = "No cooking time specified"
        else:
            time_str = f"{self.__cooking_time} minutes to cook"

        if len(self.__ingredients) == 0:
            ingredient_str = "\n  No ingredients"
        else:
            plural = "s" if len(self.__ingredients) > 1 else ""
            ingredient_str = f"\n{len(self.__ingredients)} Ingredient{plural}:"
            for ingredient, quantity in self.__ingredients.items():
                ingredient_str += f"\n  {ingredient}: {quantity}"

        if len(self.__instructions) == 0:
            instruction_str = "\n  No instructions"
        else:
            instruction_str = "\nInstructions:"
            for i, instruction in enumerate(self.__instructions):
                instruction_str += f"\n  {i + 1}. {instruction}"

        return f"{self.name}:\n  ({time_str})\n{ingredient_str}\n{instruction_str}"
