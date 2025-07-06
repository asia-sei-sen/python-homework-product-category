import pytest
from product import Product, Smartphone, LawnGrass
from category import Category


def test_add_same_class_products():
    phone1 = Smartphone("Phone A", "Desc", 100, 5, 90, "X1", 64, "Black")
    phone2 = Smartphone("Phone B", "Desc", 200, 3, 85, "X2", 128, "White")
    total = phone1 + phone2
    assert total == 100*5 + 200*3


def test_add_different_class_products_raises():
    phone = Smartphone("Phone A", "Desc", 100, 5, 90, "X1", 64, "Black")
    grass = LawnGrass("Grass A", "Desc", 50, 10, "CountryX", 7, "Green")
    with pytest.raises(TypeError):
        _ = phone + grass


def test_add_product_rejects_non_product():
    category = Category("Test Category", "Description")
    phone = Smartphone("Phone A", "Desc", 100, 5, 90, "X1", 64, "Black")
    category.add_product(phone)  # OK
    with pytest.raises(TypeError):
        category.add_product("not a product")

