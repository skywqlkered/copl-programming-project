from Recipe import Recipe
from User import User

class MealPlan:
    """Class containing methods to plan meals for a person"""
    def __init__(self):
        pass

class GroupMealPlan(MealPlan):
    """
    Class containing methods to plan meals for gorups
    Inherits from MealPlan
    """
    def __init__(self):
        super().__init__()