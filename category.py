from product import Product

class Category:
    total_categories = 0      # общее количество категорий
    total_products = 0        # общее количество товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(products)
