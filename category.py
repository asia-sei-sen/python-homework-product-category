from product import Product


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # приватный список
        Category.total_categories += 1

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self):
        try:
            total = sum(product.price for product in self.__products)
            count = len(self.__products)
            return total / count
        except ZeroDivisionError:
            return 0
