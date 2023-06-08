from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        """
        Initializes a new instance of the Store class.

        Args:
            products (List[Product]): The initial list of products in the store.
        """
        self.product_list = products

    def add_product(self, product: Product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add.
        """
        self.product_list.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.
        """
        if product in self.product_list:
            self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Retrieves a list of all active products in the store.

        Returns:
            List[Product]: The list of active products in the store.
        """
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Places an order for a list of products with their quantities.

        Args:
            shopping_list (List[tuple]): The list of products and their quantities to order.

        Returns:
            float: The total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.product_list:
                try:
                    total_price += product.buy(quantity)
                except Exception as e:
                    print(f"Failed to order product {product.name}: {str(e)}")
        return total_price
