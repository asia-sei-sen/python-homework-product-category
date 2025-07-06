from product import Product
from category import Category

def test_product_str():
    p = Product("Яблоко", "Свежее яблоко", 100, 10)
    assert str(p) == "Яблоко, 100 руб. Остаток: 10 шт."

def test_category_str():
    c = Category("Фрукты", "Категория свежих фруктов")
    c.add_product(Product("Яблоко", "Свежее", 100, 10))
    c.add_product(Product("Груша", "Сладкая", 120, 5))
    assert str(c) == "Фрукты, количество продуктов: 15 шт."

def test_product_add():
    p1 = Product("Молоко", "1 л", 80, 3)
    p2 = Product("Кефир", "1 л", 60, 2)
    assert p1 + p2 == 80 * 3 + 60 * 2  # 240 + 120 = 360
