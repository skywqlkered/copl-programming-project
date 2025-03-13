from Ingredient import Ingredient

class Recipe:
    """
    A recipe for a dish.
    Includes a name, cooking time, a list of ingredients, and a list of instructions.
    """
    def __init__(self, name: str, people_count: int, cooking_time: int = None):
        """
        Initializes a Recipe object.

        Args:
            name (str): The name of the recipe.
            cooking_time (int) (optional): The time it takes to cook the recipe in minutes.
        """

        if isinstance(people_count, int) or isinstance(people_count, type(None)):
            self.__people_count = people_count
        else:
            raise ValueError(f"Cooking time must be an integer or None. (currently {type(cooking_time)}: {cooking_time})")

        if isinstance(cooking_time, int) or isinstance(cooking_time, type(None)):
            self.__cooking_time = cooking_time
        else:
            raise ValueError(f"Cooking time must be an integer or None. (currently {type(cooking_time)}: {cooking_time})")
        
        self.name = name
        self.__ingredients = {}
        self.__instructions = []

    def ingredients(self, people_count: int = None):
        """
        Returns the list of ingredients needed for the recipe.
        
        Args:
            people_count (int) (optional): The number of people the recipe is for.
        """
        if people_count != None:
            ingredients = {}
            for ingredient, quantity in self.__ingredients.items():
                q = round(quantity / self.__people_count * people_count, 2)
                if q % 1 == 0:
                    q = int(q)
                ingredients[ingredient] = q
            return ingredients
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

    def for_persons(self, people_count: int):
        """Returns a string representation of the recipe for a certain number of people."""
        return self.__print_str(people_count)

    def change_people_count(self, people_count: int):
        """Changes the number of people the recipe is for."""
        self.__ingredients = self.ingredients(people_count)
        self.__people_count = people_count

    def __print_str(self, people_count: int):
        """Prints the recipe in a readable format."""
        # Cooking time
        if self.__cooking_time is None:
            time_str = "No cooking time specified"
        else:
            time_str = f"{self.__cooking_time} minutes to cook"

        # Ingredients
        if len(self.__ingredients) == 0:
            ingredient_str = "\n  No ingredients"
        else:
            plural = "s" if len(self.__ingredients) > 1 else ""
            ingredient_str = f"\n{len(self.__ingredients)} Ingredient{plural}:"
            for ingredient, quantity in self.ingredients(people_count).items():
                ingredient_str += f"\n  {ingredient}: {quantity}"

        # Instructions
        if len(self.__instructions) == 0:
            instruction_str = "\n  No instructions"
        else:
            instruction_str = "\nInstructions:"
            for i, instruction in enumerate(self.__instructions):
                instruction_str += f"\n  {i + 1}. {instruction}"

        # Persons
        person = "persons" if people_count > 1 else "person"

        return f"{self.name}:\n  ({people_count} {person}, {time_str})\n{ingredient_str}\n{instruction_str}"

    def __str__(self):
        return self.__print_str(self.__people_count)
