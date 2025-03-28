from Json import Json # add data, get data
from User import User # add recipe, remove recipe, add shopping list, remove shopping list
from RecipeBook import RecipeBook # add recipe, remove recipe
from Shoppinglist import Shoppinglist # add item, remove item
from Refrigerator import Refrigerator # add item, remove item
from Shelf import Shelf
from Recipe import Recipe # add ingredient, remove ingredient
from Ingredient import Ingredient # add item, remove item
from MealPlan import MealPlan # add recipe, remove recipe
from datetime import datetime

class Backend:
    def __init__(self):
        self.user: User = None

    def save_userinstance(self):
        user = self.user
        a = Json()
        a.write_data(user.name, user.mealplan, user._shoppinglist.ingredients, user.recipebooks, user.storage)

    def get_userinstance(self, name: str):
        a = Json()
        data = a.get_user_data(name)
        return data

    def _set_meanplan_of_user(self, user: User):
        """
        Sets the meal plan of a user by retrieving the data from the user instance and creating a MealPlan instance from it.

        Args:
            user (User): The user for whom the meal plan will be set.

        The meal plan is created by iterating over a provided data structure, extracting recipe names, cooking times, people counts,
        ingredients, and instructions, then creating Recipe instances and adding them to a MealPlan, which is then assigned to the user's meal plan attribute.
        """
        userdata: dict = self.get_userinstance(user.name)


        plan = MealPlan(len(userdata["mealplan"].keys()))
        
        for key,value in userdata["mealplan"].items():
            day = key
            recipename = value[0]
            cookingtime = value[1]
            peoplecount = value[2] 
            ingredients = value[3]
            instructions = value[4]

            recipe = Recipe(recipename, peoplecount, cookingtime)
            for instruction in instructions:
                recipe.add_instruction(instruction)

            for key, value in ingredients.items():
                recipe.add_ingredient(ingredient=key, quantity=value)

            plan.add_meal(day, recipe)
        user.mealplan = plan

    def _add_recipebooks_to_user(self, user: User):
        """
        Adds recipe books to a user by creating RecipeBook instances from provided data and adding them to the user's collection.

        Args:
            user (User): The user to whom the recipe books will be added.

        Each recipe book is created by iterating over a provided data structure, extracting recipe names, cooking times, people counts,
        ingredients, and instructions, then creating Recipe instances and adding them to a RecipeBook, which is then added to the user's collection.
        """
        data = self.get_userinstance(user.name)

        recipbook = RecipeBook()
        for key,value in data["recipebooks"].items():
            recipename = key
            cookingtime = value[0]
            peoplecount = value[1] 
            ingredients = value[2]
            instructions = value[3]

            recipe = Recipe(recipename, peoplecount, cookingtime)
            for instruction in instructions:
                recipe.add_instruction(instruction)
    
            for key, value in ingredients.items():
                recipe.add_ingredient(ingredient=key, quantity=value)

            recipbook.add_recipe(recipe)
        user.add_recipebook(recipbook)

    def _set_shoppinglist_of_user(self, user: User):
        userdata: dict = self.get_userinstance(user.name)
        shoppinglist: Shoppinglist = Shoppinglist()
        for key, value in userdata["shoppinglist"].items():
            ing: Ingredient = Ingredient(key, value[0][0])
            ing.expiration_date = datetime.strptime(value[0][1], "%Y-%m-%d")
            ing.quantity = value[0][2]

            shoppinglist.add_ingredient(ingredient=ing, amount=value[1])
        user._shoppinglist = shoppinglist


    def _set_storage_of_user(self, user: User):
        userdata: dict = self.get_userinstance(user.name)
        for storage_type, value in userdata["storage"].items():
            if storage_type == "refrigerators":	
                used_space = 0                
                if len(value) > 0:
                    for name, ingredient in value[1].items():
                        ing = Ingredient(name, ingredient[0])
                        ing.expiration_date = datetime.strptime(ingredient[1], "%Y-%m-%d")
                        ing.quantity = ingredient[2]
                        used_space += ing.quantity
                    a = Refrigerator(value[0] + used_space)
                    a.add_ingredient(ing)
                    a.temperature = value[2]
                    user.add_refrigerator(a)
            elif storage_type == "shelves":
                used_space = 0
                if len(value) > 0:
                    for name, ingredient in value[1].items():
                        ing = Ingredient(name, ingredient[0])
                        ing.expiration_date = datetime.strptime(ingredient[1], "%Y-%m-%d")
                        ing.quantity = ingredient[2]
                        used_space += ing.quantity
                    a = Shelf(value[0])
                    a.add_ingredient(ing)
                    user.add_shelf(a)

    def setup_all(self, user: User):
        self._set_meanplan_of_user(user)
        self._add_recipebooks_to_user(user)
        self._set_shoppinglist_of_user(user)
        self._set_storage_of_user(user)

    def create_recipe(self, rname = None, peopl = None, time = None):
        if not rname:
            rname = input("Whats the name of the recipe (enter q to go back): ")
        if rname == "q":
            return
        while not peopl:
            peopl = input("For how many people is this recipe: ")
            peopl = self.int_try(peopl)

        while not time:
            time = input("How many minutes will it take to make this recipe: ")
            time = self.int_try(time)        

        r = Recipe(rname, peopl, time)
        print("Enter ingredients:")
        while True:
            choice = input("Enter an ingredient (enter q to stop): ")
            if choice == "q":
                break
            ing = self.ingredient_maker(choice)
            r.add_ingredient(ing, ing.quantity)

        print("Enter instructions:")
        while True:
            choice = input("Enter an instruction step (enter q to stop): ")
            if choice == "q":
                break
            r.add_instruction(choice)
        return r

    def ingredient_maker(self, ingname=None, quantity = None):
        """
        Prompts the user for an ingredient name and quantity, and then creates and returns an Ingredient object with the given name and quantity.

        If the user enters an invalid quantity, this function will call itself with the invalid input and try again.
        
        Args:
            quantity (int, optional): The quantity of the ingredient. If not provided, the user will be prompted to enter it.
        
        Returns:
            Ingredient: The created Ingredient object.        
        """
        if not ingname:
            ingname = input("Ingredient name: ")
        while not quantity:
            quantity = input("Quantity: ")
            quantity = self.int_try(quantity)

        ing = Ingredient(ingname)
        ing.quantity = quantity
        return ing

    def int_try(self, intinput: str):
        """
        Attempts to convert a string input to an integer. If the conversion fails, 
        it calls the provided function with additional arguments.

        Args:
            intinput (str): The input string to be converted to an integer.
            func (callable): The function to call if the conversion fails.
            *args: Additional positional arguments for the function.
            **kwargs: Additional keyword arguments for the function.

        Returns:
            int: The converted integer if successful.
        """

        try:
            return int(intinput)
        except ValueError:
            print("\nPlease enter a valid number\n")
            return False

    def add_recipe_to_recipebook(self):
        print("What recipe would you like to add?")
        recipes = self.list_all_recipes(True)
        for  i, recipe in enumerate(recipes):
            print(f"{i+1}. {recipe}")

    def remove_recipe_from_recipebook(self):
        print("What recipe would you like to remove?")
        recipes = self.list_all_recipes()
        for i, recipe in enumerate(recipes):
            print(f"{i+1}. {recipe}")

        while True:
            choice = input("Enter the number of the recipe you want to remove: ")
            if choice in [str(i) for i in range(1, len(recipes) + 1)]:
                break

        
        self.user.recipebooks[0].remove_recipe(recipes[int(choice) - 1])

    def find_recipe_by_name(self):
        pass

    def find_recipe_by_ingredient(self):
        pass

    def find_recipe_by_cooking_time(self):
        pass

    def list_all_recipes(self, boolean = None):
        """
        Lists all recipes in the recipe book.

        Args:
            boolean (bool): If True, the function will only list recipes that are not in any recipe book.

        Returns:
            list: A list of recipe names.
        """
        
        if boolean: # will list all unused recipes in the recipe book
            return [recipe.name for recipe in self.user.recipebooks[0]]
        
        full_list = []
        for book in self.user.recipebooks:
            for recipename in book.list_recipes():
                full_list.append(recipename)
        return full_list
    


    if __name__ == "__main__":
        # a = Interface()

        # recipe = Recipe("apple pie", 3)
        # recipe.add_ingredient(Ingredient("apple"), 32)
        # recipe.add_instruction("Bake the pie")
        # recipe.add_instruction("Cut the pie")

        # rock = Recipe("Rock", 18)
        # rock.add_ingredient(Ingredient("dirt"), 60)
        # rock.cooking_time = 180
        # rock.add_instruction("Dig a hole")
        # rock.add_instruction("Gather the dirt and rocks")
        # rock.add_instruction("Mix and enjoy")

        # recipeBook = RecipeBook()
        # recipeBook.add_recipe(recipe)
        # recipeBook.add_recipe(rock)

        # ing = Ingredient("apple")
        # ing.quantity = 6
        # ing.expiration_date = datetime.today()
        # ing.temperature = 5

        # frige = Refrigerator(8)
        # frige.add_ingredient(ing)

        # a.user = User("Marc")
        # a.user.mealplan = MealPlan()
        # a.user.mealplan.add_meal("Monday", recipe)
        # a.user.mealplan.add_meal("Tuesday", rock)
        # a.user.add_recipebook(recipeBook)
        # a.user._shoppinglist = Shoppinglist()
        # a.user._shoppinglist.add_ingredient(ing, 7)
        # a.user.add_refrigerator(frige)

        # a.save_userinstance()

        # a = Interface()
        # userdata: dict = a.get_userinstance("Marc")


        # Marc = User(userdata["name"])
        # a._set_storage_of_user(Marc)

        # print(Marc.storage)
        j = User("John")
        j.add_refrigerator(Refrigerator(1000))

        banana = Ingredient("banana", temperature=4)
        banana.expiration_date = datetime.now()
        banana.quantity = 5

        # j.storage["refrigerators"][0].add_ingredient(banana)
        print(j.has_item())
        print(j.has_item("banana"))
        print(j.has_item("apple"))