from Recipe import Recipe

class RecipeBook:
    """
    A collection of recipes that allows adding, removing, searching, and listing recipes.
    """
    def __init__(self):
        """Initializes an empty recipe book."""
        self.__recipes = {}

    @property
    def recipes(self):
        return self.__recipes

    def add_recipe(self, recipe):
        """
        Adds a recipe to the recipe book.

        Args:
            recipe (Recipe): The recipe to add.
        """
        if not isinstance(recipe, Recipe):
            raise ValueError("Only Recipe objects can be added.")
        self.__recipes[recipe.name] = recipe

    def remove_recipe(self, recipe_name):
        """
        Removes a recipe from the recipe book.

        Args:
            recipe_name (str): The name of the recipe to remove.
        """
        if recipe_name in self.__recipes:
            del self.__recipes[recipe_name]
        else:
            raise ValueError(f"No recipe found with name '{recipe_name}'.")

    def find_recipe(self, recipe_name):
        """
        Finds a recipe by its name.

        Args:
            recipe_name (str): The name of the recipe to find.

        Returns:
            Recipe: The recipe if found, otherwise None.
        """
        return self.__recipes.get(recipe_name, None)

    def list_recipes(self):
        """
        Lists all recipe names in the recipe book.

        Returns:
            list: A list of recipe names.
        """
        return list(self.__recipes.keys())

    def search_by_ingredient(self, ingredient_name):
        """
        Finds all recipes that contain a specific ingredient.

        Args:
            ingredient_name (str): The ingredient to search for.

        Returns:
            list: A list of recipe names that include the ingredient.
        """
        matching_recipes = []
        for recipe in self.__recipes.values():
            if ingredient_name in (ing for ing in recipe.ingredients()):
                matching_recipes.append(recipe.name)
        return matching_recipes

    def recipes_under_time(self, max_time):
        """
        Finds all recipes that have a cooking time less than the specified time.

        Args:
            max_time (int): The maximum cooking time in minutes.

        Returns:
            list: A list of recipe names that take less than max_time to cook.
        """
        return [recipe.name for recipe in self.__recipes.values() if recipe.cooking_time and recipe.cooking_time < max_time]

    def __str__(self):
        """Returns a string representation of the recipe book."""
        if not self.__recipes:
            return "The recipe book is empty."
        return "Recipe Book:\n" + "\n".join(f"- {name}" for name in self.__recipes.keys())
