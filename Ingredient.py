from datetime import date


class Ingredient:
    def __init__(self, name: str, max_temperature: int):
        self.name = name
        self.max_temperature = max_temperature
        self.__expiration_date = date.today()
        self.__quantity = 0

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity > 0:
            self.__quantity = quantity

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, day: date):
        try:
            date(day)
            self.__expiration_date = day
        except ValueError:
            raise ValueError("This is not of the form (year, month, day)")

    def add(self, amount: int):
        if amount > 0:
            self.__quantity += amount
        else:
            raise ValueError("Amount not larger than zero")

    def remove(self, amount: int):
        if amount <= self.__quantity and amount > 0:
            self.__quantity -= amount
        else:
            raise ValueError(
                f"Amount not higher than zero or not lower than or equal to current quantity, which is {self.__quantity}")

    def __str__(self):
        return f"{self.name}: {self.quantity} g. Kept at {self.temperature} degrees till {self.expiration_date}"
    
    def __eq__(self, another):
        if self.name == another.name and self.expiration_date == another.expiration_date and self.temperature == another.temperature:
            return True
        else:
            return False

    def __le__(self, another):
        if self.__quantity <= another.__quantity:
            return True
        else:
            return False

    def __ge__(self, another):
        if self.__quantity >= another.__quantity:
            return True
        else:
            return False
