from abc import ABC, abstractmethod

# 1. Абстрактный базовый класс


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @abstractmethod
    def __str__(self):
        pass


# 2. Миксин
class LogMixin:
    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        args_str = ", ".join(repr(arg) for arg in args)
        print(f"{cls_name}({args_str})")
        super().__init__(*args, **kwargs)


# 3. Product с множественным наследованием
class Product(LogMixin, BaseProduct):
    @classmethod
    def new_product(cls, data_dict):
        return cls(
            name=data_dict["name"],
            description=data_dict["description"],
            price=data_dict["price"],
            quantity=data_dict["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity


# 4. Наследники
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
