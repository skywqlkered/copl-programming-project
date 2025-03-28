
import json

class Json:
    def __init__(self):
        self.data = self.get_existing_data()

    def get_existing_data(self):
        file = "data.json"

        with open(file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def get_user_data(self, username: str):
        """Retrieves data for a specific user."""
        return self.data.get(username, None)
            

    def write_data(self, *data):
        username = data[0]

        self.data[username] = json.loads(self._format(data))

        file = open("data.json", "w")
        json.dump(self.data, file, indent=4)
        file.close()
        




    def _format(self, *args):
        if len(args[0]) != 5:
            raise ValueError("Data must be a tuple of 5 elements.")
        user = args[0][0]
        mealprep = args[0][1]
        shoppinglist = args[0][2]
        recipebook = args[0][3]
        storage = args[0][4]

        formatted_meanplan = {}
        if not mealprep: # if the meal plan is empty, return an empty dictionary
            return formatted_meanplan
        for day, recipe in mealprep.meals.items():
            if recipe:
                formatted_meanplan[day] = recipe.name, recipe.cooking_time, recipe.people_count, recipe.ingredients(), recipe.instructions

        formattted_shoppinglist = {}
        for storage_type, value in shoppinglist.items():
            formattted_shoppinglist[storage_type] = [value[0][0], (str(value[0][1])).split(" ")[0], value[0][2]], value[1]

        formatted_recipebook = {}
        for recipe in recipebook.recipes:
            if recipe:
                usable_recpipe = recipebook.recipes[recipe]
                formatted_recipebook[recipebook.recipes[recipe].name] = usable_recpipe.cooking_time, usable_recpipe.people_count, usable_recpipe.ingredients(), usable_recpipe.instructions

        formatted_storage = {"refrigerator": [], "shelf": []}         
        for storage_type, storage in storage.items():
            formatted_ing = {}
            if storage:
                for ingredient in storage._ingredients:
                    formatted_ing[ingredient.name] = [ingredient.temperature, (str(ingredient.expiration_date)).split(" ")[0], ingredient.quantity]
                try:
                    formatted_storage[storage_type] = storage.storage_space, formatted_ing, storage.temperature
                except: #noqa
                    formatted_storage[storage_type] = storage.storage_space, formatted_ing, None

        formatted_data = {
            "name": user,
            "mealplan": formatted_meanplan,
            "shoppinglist": formattted_shoppinglist,
            "recipebook": formatted_recipebook,
            "storage": formatted_storage
        }
        return json.dumps(formatted_data, indent=4)


