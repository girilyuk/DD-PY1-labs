class Coffee:
    """Базовый класс для кофе"""

    def __init__(self, name: str, origin: str, roast_level: str) -> None:
        """Инициализация атрибутов кофе"""
        self.name = name
        self.origin = origin
        self.roast_level = roast_level

    def __str__(self) -> str:
        """Возвращает строковое представление кофе"""
        return f"{self.name} страна {self.origin} с ароматом {self.roast_level}"

    def __repr__(self) -> str:
        """Возвращает подробное представление кофе"""
        return f"Coffee(name='{self.name}', origin='{self.origin}', roast_level='{self.roast_level}')"

class Cappuccino(Coffee):
    """Класс капучино, наследуется от Coffee"""

    def __init__(self, origin: str, roast_level: str, syrup: float) -> None:
        """Инициализация атрибутов кофе"""
        super().__init__("Капучино", origin, roast_level)
        self.__syrup = syrup  # Инкапсуляция, чтобы сироп не менялось вне класса

    def __str__(self) -> str:
        """Возвращает строковое представление капучино с сиропом"""
        return f"{super().__str__()} с сироппом {self.__syrup} мл"

    def __repr__(self) -> str:
        """Возвращает подробное представление капучино"""
        return f"Cappuccino(origin='{self.origin}', roast_level='{self.roast_level}', syrup={self.__syrup})"

    def info(self) -> str:
        """Возвращает информацию о капучино"""
        return f"{self.name} страна {self.origin}, аромат: {self.roast_level}, сироп: {self.__syrup} мл"

class Espresso(Coffee):
    """Класс эспрессо, наследуется от Coffee"""

    def __init__(self, origin: str, roast_level: str, portion: str) -> None:
        """Инициализация атрибутов эспрессо"""
        super().__init__("Эспрессо", origin, roast_level)
        self.portion = portion  # Доступен для изменения, так как его изменение может быть полезным

    def __str__(self) -> str:
        """Возвращает строковое представление эспрессо с порцией"""
        return f"{super().__str__()} порция: {self.portion}"

    def __repr__(self) -> str:
        """Возвращает подробное представление эспрессо"""
        return f"Espresso(origin='{self.origin}', roast_level='{self.roast_level}', portion='{self.portion}')"

    def info(self) -> str:
        """Возвращает информацию о эспрессо"""
        return f"{self.name} страна {self.origin}, аромат: {self.roast_level}, порция: {self.portion}"

if __name__ == "__main__":
    cappuccino = Cappuccino("Италия", "Средняя", 5)
    espresso = Espresso("Эфиопия", "Контрастный", "Х2")

    print(cappuccino)
    print(repr(cappuccino))
    print(cappuccino.info())

    print(espresso)
    print(repr(espresso))
    print(espresso.info())