from Recipe import Recipe
from Shoppinglist import Shoppinglist
from Ingredient import Ingredient

class MealPlan:
    """Class containing methods to plan meals for a person"""

    standard_week = 7

    def __init__(self, days: int = standard_week):
        """
        Initializes a MealPlan for a user.

        Args:
            user (User): A user for whom the Mealplan is.
            days (int, optional): The amount of days to plan, starting on monday. Defaults to standard_week (a full week).
        """
        self._days = days
        self.meals: dict[str, Recipe] = {}
        self._initialize_days()

    def _initialize_days(self):
        """Initializes the meal plan with empty meals (None) for each day."""
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(self._days):
            self.meals[days_of_week[i % 7]] = None

    def add_meal(self, day: str, recipe: Recipe):
        """
        Adds a recipe to a specific day in the meal plan.
        
        Args:
            day (str): The day to add a recipe to
            recipe (Recipe): The recipe for the meal to assign to the day
        """
        if day in self.meals:
            self.meals[day] = recipe
        else:
            print(f"Error: {day} is not a valid day in this meal plan.")

    def generate_shopping_list(self):
        """
        Generates a shopping list based on the meal plan.
        
        Returns:
            Shoppinglist: A shoppinglist object containing all ingredients.
        """
        all_ingredients = {}
        for recipe in self.meals.values():
            if recipe is not None:
                for ingredient, quantity in recipe.ingredients().items():
                    if ingredient in all_ingredients:
                        all_ingredients[ingredient] += quantity
                    else:
                        all_ingredients[ingredient] = quantity

        shopping_list = Shoppinglist()
        for ingredient, quantity in all_ingredients.items():
            shopping_list.add_ingredient(Ingredient(ingredient), quantity)
        return shopping_list

    @staticmethod
    def calculate_total_cooking_time(meal_plan):
        """
        Calculates the total cooking time for all meals in a meal plan.
        
        Returns:
            int: the total time in minutes to cook during a mealplan
        """
        total_time = 0
        for recipe in meal_plan.meals.values():
            if recipe is not None and recipe.cooking_time is not None:
                total_time += recipe.cooking_time
        return total_time

    @classmethod
    def create_short_plan(cls):
        """
        Creates a meal plan for 3 days.
        
        Returns:
            MealPlan: A mealplan instance for 3 days
        """
        return cls(days=3)

    def __str__(self):
        """
        Prints the meal plan in a readable format.
        
        Returns:
            str: The meal plan in readable format
        """
        plan_string = "Meal Plan:\n"
        for day, recipe in self.meals.items():
            if recipe is not None:
                plan_string += f"{day}: {recipe.name}\n{recipe}\n------\n"
            else:
                plan_string += f"{day}: No meal planned.\n"
        return plan_string
    
    def __repr__(self):
        """
        Returns a string representation of the meal plan.
        
        Returns:
            str: A string representation of the meal plan.
        """ 
        mealplan = []
        for i, k in self.meals.items():
            mealplan.append((i, k))
        return str(mealplan)


