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
        a.write_data(user.name, user.mealplan, user._shoppinglist.ingredients, user.recipebook, user.storage)

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

    def _add_recipebook_to_user(self, user: User):
        """
        Adds recipe books to a user by creating RecipeBook instances from provided data and adding them to the user's collection.

        Args:
            user (User): The user to whom the recipe books will be added.

        Each recipe book is created by iterating over a provided data structure, extracting recipe names, cooking times, people counts,
        ingredients, and instructions, then creating Recipe instances and adding them to a RecipeBook, which is then added to the user's collection.
        """
        data = self.get_userinstance(user.name)

        recipbook = RecipeBook()
        for key,value in data["recipebook"].items():
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
            if storage_type == "refrigerator" and value:	
                used_space = 0                
                if len(value[1]) > 0:
                    for name, ingredient in value[1].items():
                        ing = Ingredient(name, ingredient[0])
                        ing.expiration_date = datetime.strptime(ingredient[1], "%Y-%m-%d")
                        ing.quantity = ingredient[2]
                        used_space += ing.quantity
                    a = Refrigerator(value[0] + used_space)
                    a.add_ingredient(ing)
                    a.temperature = value[2]
                    user.add_refrigerator(a)
                else:
                    a = Refrigerator(value[0])
                    a.temperature = value[2]
                    user.add_refrigerator(a)
            elif storage_type == "shelf" and value:
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
                else:
                    a = Shelf(value[0])
                    user.add_shelf(a)

    def setup_all(self, user: User):
        self._set_meanplan_of_user(user)
        self._add_recipebook_to_user(user)
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

    def int_value_try(self, intinput: str, min_value, max_value):
        try:
            int_value = int(intinput)
        except ValueError:
            print("\nPlease enter a valid number\n")
            return False
        if int_value >= min_value and int_value <= max_value:
            return int_value
        else:
            print(f"\n Please enter a number between {min_value} and {max_value}\n")
    def add_recipe_to_recipebook(self):
        print("What recipe would you like to add?")
        recipes: list[str] = self.list_all_recipes()
        for i, recipe in enumerate(recipes):
            print(f"{i+1}. {recipe.name}")

        while True:
            choice = input("Enter the number of the recipe you want to add: ")
            if choice in [str(i) for i in range(1, len(recipes) + 1)]:
                break
        self.user.recipebook.add_recipe(recipes[int(choice) - 1])

    def remove_recipe_from_recipebook(self):
        print("What recipe would you like to remove?")
        recipes = self.list_all_recipes()
        for i, recipe in enumerate(recipes):
            print(f"{i+1}. {recipe}")

        while True:
            choice = input("Enter the number of the recipe you want to remove: ")
            if choice in [str(i) for i in range(1, len(recipes) + 1)]:
                break
        self.user.recipebook.remove_recipe(self.user.recipebook.list_recipes()[int(choice) - 1].name)

    def find_recipe_by_name(self):
        recipname = input("Enter the name of the recipe you want to search for: ")
        return self.user.recipebook.find_recipe(recipname)

    def find_recipe_by_ingredient(self):
        ingname = input("Enter the name of the ingredient you want to search for : ")
        return self.user.recipebook.search_by_ingredient(ingname)
    
    def find_recipe_by_time(self, time=None):
        while not time:
            time = input("Enter the time you want to search for: ")
            time = self.int_try(time)
        return self.user.recipebook.recipes_under_time(time)


    def list_all_recipes(self) -> list[Recipe]:
        """
        Lists all recipes in the recipe book.

        Args:
            boolean (bool): If True, the function will only list recipes that are not in any recipe book.

        Returns:
            list: A list of recipe names.
        """
        full_list = []
        for rname, recipe in self.user.recipebook.recipes.items():
            full_list.append(recipe)
        return full_list
    
    def add_shelf(self, storage_space = None):
        while not storage_space:
            print("Enter storage space of shelf:")
            storage_space = self.int_try(input())
        shelf = Shelf(storage_space)
        self.user.add_shelf(shelf)

    def add_refrigerator(self, storage_space = None, temperature = None):
        while not storage_space:
            print("Enter storage space of refrigerator:")
            storage_space = self.int_value_try(input(), 0, 500)
        while not temperature:
            print("Enter temperature of the refrigerator:")
            temperature = self.int_value_try(input(), 0, 8)
        refrigerator = Refrigerator(storage_space)
        refrigerator.temperature = temperature
        self.user.add_refrigerator(refrigerator)

    def add_ingredient_storage(self, temperature = None, date = None):
        ingredient = self.ingredient_maker()
        while not temperature:
            print("Temperature at which the ingredient should be kept: ")
            temperature = self.int_value_try(input(), 0, 30)
        ingredient.temperature = temperature
        while not date:
            print("Expiration date:")
            year = input("Year: ")
            month = input("Month: ")
            day = input("Day: ")
            try:
                ingredient.expiration_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
                date = True
            except: #noqa
                print("\nEnter valid experation date.\n")
        
        if ingredient.temperature:
            try:
                self.user.storage["refrigerator"].add_ingredient(ingredient)
                print("Ingredient added to refrigerator.")
            except ValueError:
                try:
                    self.user.storage["shelf"].add_ingredient(ingredient)
                    print("Ingredient added to shelf.")
                except ValueError:
                    print("Shelf is full.")
                except AttributeError:
                    print("You have no shelf yet.")
            except AttributeError:
                print("You have no refrigerator yet.")

    def remove_ingredient_from_storage(self):
        ingredient = self.ingredient_maker()
        try:
            self.user.storage["shelf"].remove_ingredient(ingredient)
            
        except AttributeError:
            try:
                self.user.storage["refrigerator"].remove_ingredient(ingredient)
                
            except AttributeError:
                print("This item is not in your storage.")
        

    def check_bad_ingredients(self):
        #shelf
        if self.user.storage["shelf"]:
            if len(self.user.storage["shelf"].bad_ingredients()) != 0:
                expired_ingredients, refrigerator_ingredients = self.user.storage["shelf"].bad_ingredients()
                print("Expired ingredients in shelf:")
                for ingredient in expired_ingredients:
                    print(ingredient)
                print("Ingredients in shelf that should be in refrigerator:")
                for ingredient in refrigerator_ingredients:
                    print(ingredient)
            else: 
                print("No expired ingredients in shelf.")
        else:
            print("You have no shelf yet.")

        #refrigerator
        if self.user.storage["refrigerator"]:
            if len(self.user.storage["refrigerator"].bad_ingredients()) != 0:

                bad_ingredients = self.user.storage["refrigerator"].bad_ingredients()
                print("Expired ingredients in refrigerator:")
                for ingredient in bad_ingredients:
                    print(ingredient)

            else:
                print("No expired ingredients in refrigerator.")
        else:
            print("You have no fridge yet.")

    def create_mealplan(self, days=None):
        while not days:
            days = input("Enter the number of days you want to plan: ")
            days = self.int_try(days)
        self.user.mealplan = MealPlan(days)

        while True:
            choice = input("Would you like to add a recipe to your mealplan? (y/n): ")
            if choice.lower() == "y":
                self.add_recipe_to_mealplan()
            elif choice.lower() == "n":
                break
    
    def add_recipe_to_mealplan(self):
        daychoice = input("For which day would you like to add a recipe: ")
        while daychoice.lower() not in [x.lower() for x in self.user.mealplan.meals.keys()]:
            daychoice = input("Enter a valid day: ")
        
        choice = input("How would you like to add a recipe:\n1. By name\n2. By ingredient\n3. By time\n")
        while True:
            if choice == "1":
                recipe = self.find_recipe_by_name()
                break
            elif choice == "2":
                recipe = self.find_recipe_by_ingredient()
                break
            elif choice == "3":
                recipe = self.find_recipe_by_time()
                break
        
        daychoice = daychoice.lower().capitalize()
        if self.user.mealplan.meals[daychoice]:
            print("The is already a recipe assigned to this day.")
            return
        self.user.mealplan.add_meal(daychoice, recipe)

    def remove_recipe_from_mealplan(self):
        found_recipe = self.find_recipe_by_name()
        removalday = None
        for day, recipe in self.user.mealplan.meals.items():
            if recipe.name == found_recipe.name:
                removalday = day
                break
        if removalday:
            self.user.mealplan.meals[removalday] = None

        else:
            print("Recipe not found in mealplan.")
    
    def list_all_mealplans(self):
        print(self.user.mealplan)

    def generate_shoppinglist(self):
        print(self.user.mealplan.generate_shopping_list())

    def add_ingredient_shopping_list(self):
        ingredient = self.ingredient_maker()
        self.user._shoppinglist.add_ingredient(ingredient, ingredient.quantity)
    
    def remove_ingredient_shopping_list(self):
        ingredient = self.ingredient_maker()
        self.user._shoppinglist.rem_ingredient(ingredient.name, ingredient.quantity)

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