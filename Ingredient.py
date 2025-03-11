class Ingredient:
    def __init__(self, name: str, quantity: int, expiration_date: tuple, temperature):
        self.name = name
        self.__quantity = quantity
        self.expiration_date = expiration_date
        self.temperature = temperature

    @property    
    def quantity(self):
        return self.__quantity
    
    def add(self, amount: int):
        if amount > 0:
            self.__quantity
        else:
            raise ValueError("Amount to be added should be larger than zero.")
        
    def remove(self, amount: int):
        if amount <= self.__quantity:
            self.__quantity -= amount
        else:
            raise ValueError("Amount to be removed should be lower than or equal to current quantity")


    
