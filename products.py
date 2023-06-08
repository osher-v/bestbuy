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
        self.promotion = None
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_promotion(self):
        """
         Returns the promotion of the product.

        Returns:
         int: The promotion of the product.
         """
        return self.promotion

    def set_promotion(self, promotion):
        """
                Sets the promotion of the product.

                Args:
                     The new promotion of the product.
        """
        self.promotion = promotion

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
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Insufficient quantity available")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            self.quantity -= quantity
            return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Not Applicable"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} (Max Quantity: {self.maximum})"

    def buy(self, quantity):
        try:
            if quantity > self.maximum:
                raise Exception("Maximum quantity exceeded")
            return super().buy(quantity)
        except Exception as e:
            print(f"Failed to order product {self.name}: {str(e)}")
