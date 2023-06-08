import store
import products
import promotions


def start(store_obj):
    """
    Starts the store management system.

    Args:
        store_obj (Store): The Store object representing the store.
    """
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            products1 = store_obj.get_all_products()
            print("--- Products in Store ---")
            for product in products1:
                print(product.show())

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == "3":
            products1 = store_obj.get_all_products()
            print("--- Products in Store ---")
            for i, product in enumerate(products1):
                print(f"{i + 1}. {product.show()}")

            shopping_list = []
            while True:
                product_choice = input("Enter the product number (0 to finish): ")
                if product_choice == "0":
                    break

                try:
                    product_index = int(product_choice) - 1
                    if 0 <= product_index < len(products1):
                        quantity = int(input("Enter the quantity: "))
                        shopping_list.append((products1[product_index], quantity))
                    else:
                        print("Invalid product number")
                except ValueError:
                    print("Invalid input")

            if len(shopping_list) > 0:
                total_price = store_obj.order(shopping_list)
                print(f"Order placed! Total price: {total_price} dollars")

        elif choice == "4":
            print("Thank you for using the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
