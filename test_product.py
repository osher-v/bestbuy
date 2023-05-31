import pytest
import products


def test_create_product():
    """
    Test that creating a normal product works.
    """
    product = products.Product("Test Product", price=10.99, quantity=50)
    assert product.name == "Test Product"
    assert product.price == 10.99
    assert product.quantity == 50
    assert product.is_active()


def test_create_product_with_invalid_details():
    """
    Test that creating a product with invalid details (empty name, negative price) invokes an exception.
    """
    with pytest.raises(Exception):
        products.Product("", price=10.99, quantity=50)  # Empty name should raise an exception

    with pytest.raises(Exception):
        products.Product("Test Product", price=-10.99, quantity=50)  # Negative price should raise an exception


def test_product_reaches_zero_quantity():
    """
    Test that when a product reaches 0 quantity, it becomes inactive.
    """
    product = products.Product("Test Product", price=10.99, quantity=1)
    assert product.is_active()

    product.set_quantity(0)
    assert not product.is_active()


def test_product_purchase():
    """
    Test that product purchase modifies the quantity and returns the right output.
    """
    product = products.Product("Test Product", price=10.99, quantity=10)

    total_price = product.buy(3)
    assert total_price == 3 * 10.99
    assert product.quantity == 7


def test_buying_larger_quantity_than_exists():
    """
    Test that buying a larger quantity than exists invokes an exception.
    """
    product = products.Product("Test Product", price=10.99, quantity=5)

    with pytest.raises(Exception):
        product.buy(10)  # Trying to buy 10 quantity when only 5 exists should raise an exception
