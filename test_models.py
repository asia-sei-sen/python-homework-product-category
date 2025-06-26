import pytest
from product import Product
from category import Category

def test_product_initialization():
    p = Product("Яблоко", "Красное яблоко", 15.99, 20)
    assert p.name == "Яблоко"
    assert p.description == "Красное яблоко"
    assert p.price == 15.99
    assert p.quantity == 20

def test_category_initialization():
    p1 = Product("Яблоко", "Красное яблоко", 15.99, 20)
    p2 = Product("Груша", "Спелая груша", 20.50, 15)
    c = Category("Фрукты", "Свежие фрукты", [p1, p2])
    assert c.name == "Фрукты"
    assert c.description == "Свежие фрукты"
    assert len(c.products) == 2

def test_category_product_count():
    p1 = Product("Яблоко", "Красное яблоко", 15.99, 20)
    p2 = Product("Груша", "Спелая груша", 20.50, 15)
    c = Category("Фрукты", "Свежие фрукты", [p1, p2])
    assert len(c.products) == 2

def test_category_class_attributes():
    # Сбрасываем счетчики, чтобы тесты были независимыми
    Category.total_categories = 0
    Category.total_products = 0

    p1 = Product("Яблоко", "Красное яблоко", 15.99, 20)
    p2 = Product("Груша", "Спелая груша", 20.50, 15)
    c1 = Category("Фрукты", "Свежие фрукты", [p1, p2])
    c2 = Category("Овощи", "Свежие овощи", [])

    assert Category.total_categories == 2
    assert Category.total_products == 2

