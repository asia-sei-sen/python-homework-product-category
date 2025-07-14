import pytest
from product import Product
from category import Category


def test_product_zero_quantity_raises():
    with pytest.raises(ValueError) as excinfo:
        Product("Товар", "Описание", 100, 0)
    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"


def test_category_average_price():
    cat = Category("Категория", "Описание")
    # пустая категория — средняя цена 0
    assert cat.average_price() == 0

    # добавим товары
    p1 = Product("Товар1", "Описание1", 100, 2)
    p2 = Product("Товар2", "Описание2", 200, 3)
    cat.add_product(p1)
    cat.add_product(p2)

    expected_avg = (p1.price + p2.price) / 2
    assert cat.average_price() == expected_avg
