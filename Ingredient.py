from datetime import date


class Ingredient:
    """
    An ingredient.
    Includes a name, a max temperature at which the product should be kept, an experation date and a quantity.
    """
    def __init__(self, name: str, temperature: int):
        """
        Initializes an ingredient object.

        Args:
            name (str) - Name of the ingredient
            max_temperature (int) - Max temperature at which the ingredient should be kept
        """
        self.name = name
        self.temperature = temperature
        self.__expiration_date = date.today()
        self.__quantity = 0

    @property
    def quantity(self):
        """Returns the quantity of the ingredient"""
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of an ingredient. 
        Raises a ValueError if quantity is not higher than zero. """
        if quantity > 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity should be higher than zero.")

    @property
    def expiration_date(self):
        """Returns the expiration date of the ingredient."""
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, day: date):
        """Sets the expiration date of an ingredient.
        If the day is not convertable to a date it raises a ValueError."""
        try:
            date(day)
            self.__expiration_date = day
        except ValueError:
            raise ValueError("This is not of the form (year, month, day)")

    def add(self, amount: int):
        """Adds an amount to the quantity of an ingredient.
        Raises a ValueError if amount is not higher than zero."""
        if amount > 0:
            self.__quantity += amount
        else:
            raise ValueError("Amount not larger than zero")

    def remove(self, amount: int):
        """Remove an amount of the quantity of an ingredient.
        Raises a ValueError if amount is not higher than zero or is lower than the current quantity"""
        if amount <= self.__quantity and amount > 0:
            self.__quantity -= amount
        else:
            raise ValueError(f"Amount not higher than zero or not lower than or equal to current quantity, which is {self.__quantity}")

    def __str__(self):
        return f"{self.name}: {self.quantity} g. Kept at {self.temperature} degrees till {self.expiration_date}"
    
    def __eq__(self, another):
        """Checks if the ingredient is the same.
        For this everything should be equal except the quantity."""
        if self.name == another.name and self.expiration_date == another.expiration_date and self.temperature == another.temperature:
            return True
        else:
            return False

    def __le__(self, another):
        """Checks if there is less or equal quantity of an ingredient."""
        if self.__quantity <= another.__quantity:
            return True
        else:
            return False

    def __ge__(self, another):
        """Checks if there is more or equal quantity of an ingredient."""
        if self.__quantity >= another.__quantity:
            return True
        else:
            return False
