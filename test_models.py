from product import Product
from category import Category


def test_product_initialization():
    p = Product("Яблоко", "Красное яблоко", 15.99, 20)
    assert p.name == "Яблоко"
    assert p.description == "Красное яблоко"
    assert p.price == 15.99
    assert p.quantity == 20


def test_category_initialization_and_add_product():
    c = Category("Фрукты", "Свежие фрукты")
    p1 = Product("Яблоко", "Красное яблоко", 15.99, 20)
    p2 = Product("Груша", "Спелая груша", 20.50, 15)

    c.add_product(p1)
    c.add_product(p2)

    # Проверяем, что products возвращает строку с описанием товаров
    products_str = c.products
    assert isinstance(products_str, str)
    assert "Яблоко, 15.99 руб. Остаток: 20 шт." in products_str
    assert "Груша, 20.5 руб. Остаток: 15 шт." in products_str


def test_category_class_attributes():
    # Сбрасываем счетчики
    Category.total_categories = 0
    Category.total_products = 0

    c1 = Category("Фрукты", "Свежие фрукты")
    c2 = Category("Овощи", "Свежие овощи")

    p1 = Product("Яблоко", "Красное яблоко", 15.99, 20)
    p2 = Product("Груша", "Спелая груша", 20.50, 15)

    c1.add_product(p1)
    c1.add_product(p2)

    assert Category.total_categories == 2
    assert Category.total_products == 2


def test_product_price_setter():
    p = Product("Яблоко", "Красное яблоко", 15.99, 20)
    p.price = 25.0
    assert p.price == 25.0

    # Попытка поставить отрицательную цену - должна выводить предупреждение и не менять цену
    import sys
    from io import StringIO

    captured_output = StringIO()
    sys.stdout = captured_output

    p.price = -10

    sys.stdout = sys.__stdout__
    assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()
    assert p.price == 25.0
