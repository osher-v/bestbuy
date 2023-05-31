

class Product:
    def __init__(self, name, price, quantity):
        """
        Initializes a new instance of the Product class.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        Raises:
            Exception: If the name is empty, price is negative, or quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid input")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Returns the quantity of the product.

        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: The string representation of the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buys a certain quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Raises:
            Exception: If the quantity to buy exceeds the available quantity.

        Returns:
            float: The total price of the purchase.
        """
        if quantity > self.quantity:
            raise Exception("Insufficient quantity")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
