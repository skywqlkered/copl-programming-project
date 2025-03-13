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

        # Check if the input for people_count is valid
        if isinstance(people_count, int) or isinstance(people_count, type(None)):
            self.__people_count = people_count
        else:
            raise ValueError(f"Cooking time must be an integer or None. (currently {type(cooking_time)}: {cooking_time})")

        # Check if the input for cooking_time is valid
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

    def add_ingredient(self, ingredient: Ingredient | str, quantity: int | float):
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
            try:
                if ingredient in self.__ingredients:
                    self.__ingredients[ingredient] += quantity
                else:
                    self.__ingredients[ingredient] = quantity
            except:
                return
    
    def remove_ingredient(self, ingredient: Ingredient | str, quantity: int | float = None):
        """
        Removes an ingredient from the recipe.
        
        Args:
            ingredient (Ingredient | str): The ingredient to remove.
            quantity (int | float, optional): The amount to remove. If not provided, removes the ingredient entirely.
        
        Raises:
            ValueError: If the ingredient is not in the recipe.
        """
        try:
            ingredient_name = ingredient.name if isinstance(ingredient, Ingredient) else ingredient
        except AttributeError:
            raise ValueError("Invalid ingredient input.")

        if ingredient_name not in self.__ingredients:
            raise ValueError(f"Ingredient '{ingredient_name}' not found in the recipe.")

        if quantity is None:
            # Remove the ingredient completely
            del self.__ingredients[ingredient_name]
        else:
            if not isinstance(quantity, (int, float)):
                raise ValueError("Quantity must be an integer or a float.")
            if self.__ingredients[ingredient_name] <= quantity:
                del self.__ingredients[ingredient_name]
            else:
                self.__ingredients[ingredient_name] -= quantity

    def add_instruction(self, instruction: str):
        """
        Adds an instruction to the recipe.
        Does nothing if the input is invalid.

        Args:
            instruction (str): A step in the recipe.
        """
        if isinstance(instruction, str):
            self.__instructions.append(instruction)

    def remove_instruction(self, step: int):
        """
        Removes an instruction from the recipe by its step number (starting from 1).
        
        Args:
            step (int): The step number to remove (1-based index).

        Raises:
            ValueError: If step is not a valid number or out of range.
        """
        if not isinstance(step, int) or step < 1 or step > len(self.__instructions):
            raise ValueError(f"Invalid step number. Must be between 1 and {len(self.__instructions)}.")

        # Convert 1-based index to 0-based index and remove the instruction
        del self.__instructions[step - 1]

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

    def __eq__(self, another):
        """Checks if two recipes are the same."""
        if self.name == another.name and self.__people_count == another.__people_count and self.__cooking_time == another.__cooking_time and self.__ingredients == another.__ingredients and self.__instructions == another.__instructions:
            return True
        else:
            return False
    
    def __ne__(self, another):
        """Checks if two recipes aren't the same."""
        if self.name == another.name and self.__people_count == another.__people_count and self.__cooking_time == another.__cooking_time and self.__ingredients == another.__ingredients and self.__instructions == another.__instructions:
            return False
        else:
            return True

    def __create_new_recipe(self, people_count: int):
        """Creates a new recipe for a different amount of people."""
        new_recipe = Recipe(self.name, people_count, self.__cooking_time)
        for ingredient, amount in self.ingredients(people_count).items():
            new_recipe.add_ingredient(ingredient, amount)
        for instruction in self.__instructions:
            new_recipe.add_instruction(instruction)
        return new_recipe

    def __truediv__(self, divider: int):
        """Changes the ingredient amount"""
        if self.__people_count % divider != 0:
            raise ValueError("The divider must be a divisor of the people count.")
        new_recipe = self.__create_new_recipe(self.__people_count//divider)
        return new_recipe

    def __mul__(self, multiplier: int):
        """Changes the ingredient amount"""
        people_count = self.__people_count*multiplier
        if multiplier*self.__people_count % 1 != 0:
            raise ValueError("The resulting people count must be an integer.")
        new_recipe = self.__create_new_recipe(int(people_count))
        return new_recipe

    def __rmul__(self, multiplier: int):
        """Changes the ingredient amount"""
        people_count = self.__people_count*multiplier
        if multiplier*self.__people_count % 1 != 0:
            raise ValueError("The resulting people count must be an integer.")
        new_recipe = self.__create_new_recipe(int(people_count))
        return new_recipe
