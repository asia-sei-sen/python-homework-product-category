from product import Product
from category import Category


def main():
    # Создаём продукты
    product1 = Product("Молоко", "1 литр молока", 79.99, 10)
    product2 = Product("Хлеб", "Ржаной хлеб", 35.50, 5)

    # Создаём категорию и передаём список продуктов
    category = Category("Продукты питания", "Всё для еды", [product1, product2])

    # Выводим информацию
    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    print(f"Количество товаров: {len(category.products)}")
    for product in category.products:
        print(f"- {product.name}: {product.price} руб., в наличии {product.quantity} шт.")


if __name__ == "__main__":
    main()
