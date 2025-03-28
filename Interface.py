from User import User
from backendInterface import Backend

class Interface(Backend):
    def __init__(self):
        super().__init__()
        self.option_chooser()

    def option_chooser(self) -> tuple[str, int]:
        """
        Asks the user to choose an option.

        The user is presented with the options to create a new user, load an existing user, or exit the application.
        The user's choice is returned as a tuple containing the user's input and the number of options, which is 3.

        Returns:
            tuple[str, int]: The user's choice and the number of options.
        """
        print("Welcome to the -generic kitchen application-!")
        print("Please select an option:")
        print("1. Create a new user")
        print("2. Load an existing user")
        print("3. Exit")
        choice = input("Enter your choice: ")

        choice = self.choice_loop(choice, 3)
        if choice == 1:
            self.create_user()
            self.user_choice()
        elif choice == 2:
            try:
                self.load_user()
            except KeyError:
                print("\nThis user doesn't exist, please try again\n")
                self.option_chooser()
            else:
                self.user_choice()
        elif choice == 3:
            self.exit_choise()
    
    @staticmethod
    def choice_loop(choice, options):
        """
        Loops until a valid choice is entered.

        Args:
            choice (str): The initial choice input by the user.
            options (int): The number of available options to choose from.

        Returns:
            int: The validated choice as an integer within the range of available options.
        """

        while choice not in [str(i) for i in range(1, options + 1)]:
            choice = input("Enter a valid choice: ")
        return int(choice)

    def user_choice(self):
        print(f"\nWhat would you like to do {self.user.name}?")
        print("1. Work with recipes (Create or remove recipes, create or remove a recipebook)?")
        print("2. Work with storage (add or remove items from storage)?")
        print("3. Make a mealplan (add or remove recipes of a mealplan)?")
        print("4. Make a shoppinglist (add or remove items of a shoppinglist)?")
        print("5. Change user")
        print("6. Exit")

        choice = input("Enter your choice: ")   
        choice = self.choice_loop(choice, 6)

        if choice == 1:
            self.recipe_choice()
        elif choice == 2:
            self.storage_choice()
        elif choice == 3:
            self.mealplan_choice()
        elif choice == 4:
            self.shoppinglist_choice()
        elif choice == 5:
            self.option_chooser()
        elif choice == 6:
            self.exit_choise() 

    def recipe_choice(self, choice = None):
        
        print("1. Create a recipe")
        print("2. Add a recipe to a recipebook")
        print("3. Remove a recipe from a recipebook")
        print("4. Find a recipe by name")
        print("5. Search for a recipe by an ingredient")
        print("6. Fnd a recipe under a certain cooking time")
        print("7. List all recipes")
        print("8. Return to user menu")
        print("9. Exit"	)
        if not choice:
            choice = input("Enter your choice: ")
            choice = self.choice_loop(choice, 9)

        if choice == 1:
            r = self.create_recipe()
            self.user.recipebooks[0].add_recipe(r)
            print(f"\nRecipe {r.name} created!\n")
            self.recipe_choice()
        elif choice == 2:
            while True:
                choise = input("Would you like add an existing recipe or create a new one?\n1. Existing recipe\n2. New recipe\n3. Exit\n Enter your choise: ")
                choise = self.choice_loop(choise, 3)
                if choise == 1:
                    self.add_recipe_to_recipebook()
                    break
                elif choise == 2:
                    r = self.create_recipe()
                    self.user.recipebooks[0].add_recipe(r)
                    print(f"\nRecipe {r.name} created!\n")
                    self.recipe_choice(2)
                    break

                elif choise == 3:
                    break
            self.recipe_choice()
        
        elif choice == 3:
            self.remove_recipe_from_recipebook()
        elif choice == 4:
            self.find_recipe_by_name()
        elif choice == 5:
            self.find_recipe_by_ingredient()
        elif choice == 6:
            self.find_recipe_by_cooking_time()
        elif choice == 7:
            all = self.list_all_recipes()
            print("\nRecipe list:")
            for recipe in all:
                print(f"\t{recipe}")
            print("")
            self.recipe_choice()

        elif choice == 8:
            self.user_choice()
        elif choice == 9:
            self.exit_choise()

    

    def storage_choice(self):
        pass

    def mealplan_choice(self):
        pass

    def shoppinglist_choice(self):
        pass

    def exit_choise(self):
        """
        Exits the program and saves the user if a user is logged in.
        """
        if self.user:
            self.save_userinstance()
        print("Goodbye!")
        exit()

    def create_user(self, name=None) -> User:
        """
        Creates a new user.

        Args:
            name (str, optional): The name of the new user. If not provided it will be asked for.

        Returns:
            User: The new user instance.
        """
        if not name:
            name = input("Enter your name: ")
            self.user = User(name)
        return self.user
    
    def load_user(self, name=None) -> User:
        """
        Loads a user by name.

        Args:
            name (str, optional): The name of the user to load. If not provided it will be asked for.

        Returns:
            User: The loaded user instance.

        Raises:
            KeyError: If the user is not found.
        """
        if not name:
            name = input("Enter your name: ")
        
        userdata = self.get_userinstance(name)
        if not userdata:
            raise KeyError("User not found")
        user = User(userdata["name"])
        self.setup_all(user)
        print(f"\nWelcome {user.name}")
        self.user = user
        return self.user


a = Interface()
print()

