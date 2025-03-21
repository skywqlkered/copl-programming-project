from Ingredient import Ingredient

class Shoppinglist:
    def __init__(self):
        self.ingredients: dict[Ingredient, int] = {}

    def add_ingredient(self, name: str, amount: int):
        if amount <= 0:
            raise ValueError("Cannot add 0 or less of an item")
        if name in self.ingredients:
            self.ingredients[name] += amount
        else:
            self.ingredients[name] = amount
    def _handle_remove(self, name: str): 
        try:
            del self.ingredients[name]
        
        except KeyError:
            raise KeyError("Ingredient was not found on the shoppinglist")

    def rem_ingredient(self, name: str, amount: int =None):
        if amount:
            self.ingredients[name] -= amount
            if self.ingredients[name] <= 0:
                self._handle_remove(name)
        
        else:
            self._handle_remove(name)
        
        

    def __str__(self):
        return_str = ""
        if len(self.ingredients) == 0:
            return "Wow, such empty"
        for i in range(len(self.ingredients)):
            return_str += f"{list(self.ingredients.keys())[i]}: {list(self.ingredients.values())[i]}, " 
        return f"Shoppinglist: {return_str}"
    
    def __repr__(self):
        return self.ingredients

    def __add__(self, another):
        pass

    def __sub__(div, another):
        pass

    def __mul__(self, multipier):
        pass
    
    def __rmul__(self, multipier):
        pass


milk = Ingredient("milk", 7)
eggs = Ingredient("eggs", 21)
bread = Ingredient("bread", 21)
cheese = Ingredient("cheese", 7)
butter = Ingredient("butter", 7)

a = Shoppinglist()

a.add_ingredient(milk.name)
a.rem_ingredient(milk.name)