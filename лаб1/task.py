# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Объем занимаемой жидкости не может превышать объем стакана")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        True
        >>> glass = Glass(500, 200)
        >>> glass.is_empty_glass()
        False
        """
        return self.occupied_volume == 0

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане,
        то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        >>> glass.occupied_volume
        200
        >>> glass.add_water_to_glass(350)
        Traceback (most recent call last):
            ...
        ValueError: Объем добавляемой жидкости превышает свободное место в стакане
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        if self.occupied_volume + water > self.capacity_volume:
            raise ValueError("Объем добавляемой жидкости превышает свободное место в стакане")
        self.occupied_volume += water

    def remove_water_from_glass(self, estimate_water: float) -> float:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        200
        >>> glass.occupied_volume
        300
        >>> glass.remove_water_from_glass(400)
        Traceback (most recent call last):
            ...
        ValueError: Объем извлекаемой жидкости превышает количество воды в стакане
        """
        if not isinstance(estimate_water, (int, float)):
            raise TypeError("Извлекаемая жидкость должна быть типа int или float")
        if estimate_water < 0:
            raise ValueError("Извлекаемая жидкость должна быть положительным числом")
        if estimate_water > self.occupied_volume:
            raise ValueError("Объем извлекаемой жидкости превышает количество воды в стакане")
        self.occupied_volume -= estimate_water
        return estimate_water

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

import doctest

class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева
        :param age: Возраст дерева

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age

    def grow(self, growth: float) -> None:
        """
        Увеличение высоты дерева.

        :param growth: Увеличение высоты

        :raise ValueError: Если увеличение высоты отрицательное

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)
        >>> tree.grow(2.5)
        >>> tree.height
        13.0
        >>> tree.grow(-1)
        Traceback (most recent call last):
            ...
        ValueError: Увеличение высоты должно быть положительным
        """
        if not isinstance(growth, (int, float)):
            raise TypeError("Увеличение высоты должно быть типа int или float")
        if growth < 0:
            raise ValueError("Увеличение высоты должно быть положительным")
        self.height += growth

    def age_tree(self) -> None:
        """
        Увеличивает возраст дерева на 1 год.

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)
        >>> tree.age_tree()
        >>> tree.age
        6
        """
        self.age += 1

    def display_info(self) -> str:
        """
        Отображает информацию о дереве.

        :return: Строка с информацией о дереве

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)
        >>> tree.display_info()
        'Вид: Сосна, Высота: 10.5, Возраст: 5'
        """
        return f"Вид: {self.species}, Высота: {self.height}, Возраст: {self.age}"

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

class Love:
    def __init__(self, partner: str, duration: int, intensity: float):
        """
        Создание и подготовка к работе объекта "Любовь"

        :param partner: Имя партнёра
        :param duration: Длительность отношений в месяцах
        :param intensity: Интенсивность любви от 0.0 до 10.0

        Примеры:
        >>> love = Love("Анна", 12, 8.5)  # инициализация экземпляра класса
        """
        if not isinstance(partner, str):
            raise TypeError("Имя партнёра должно быть строкой")
        if not partner:
            raise ValueError("Имя партнёра не может быть пустым")
        self.partner = partner

        if not isinstance(duration, int):
            raise TypeError("Длительность отношений должна быть целым числом")
        if duration < 0:
            raise ValueError("Длительность отношений не может быть отрицательной")
        self.duration = duration

        if not isinstance(intensity, (int, float)):
            raise TypeError("Интенсивность любви должна быть типа int или float")
        if intensity < 0.0 or intensity > 10.0:
            raise ValueError("Интенсивность любви должна быть в диапазоне от 0.0 до 10.0")
        self.intensity = intensity

    def deepen_relationship(self, months: int) -> None:
        """
        Увеличивает длительность отношений.

        :param months: Количество месяцев, на которое увеличивается длительность

        :raise ValueError: Если количество месяцев отрицательное

        Примеры:
        >>> love = Love("Анна", 12, 8.5)
        >>> love.deepen_relationship(6)
        >>> love.duration
        18
        >>> love.deepen_relationship(-1)
        Traceback (most recent call last):
            ...
        ValueError: Количество месяцев должно быть положительным
        """
        if not isinstance(months, int):
            raise TypeError("Количество месяцев должно быть целым числом")
        if months < 0:
            raise ValueError("Количество месяцев должно быть положительным")
        self.duration += months

    def increase_intensity(self, amount: float) -> None:
        """
        Увеличивает интенсивность любви.

        :param amount: Значение, на которое увеличивается интенсивность

        :raise ValueError: Если увеличение превышает 10.0

        Примеры:
        >>> love = Love("Анна", 12, 8.5)
        >>> love.increase_intensity(1.0)
        >>> love.intensity
        9.5
        >>> love.increase_intensity(2.0)
        Traceback (most recent call last):
            ...
        ValueError: Интенсивность любви не может превышать 10.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Увеличение интенсивности должно быть типа int или float")
        if self.intensity + amount > 10.0:
            raise ValueError("Интенсивность любви не может превышать 10.0")
        self.intensity += amount

    def display_info(self) -> str:
        """
        Отображает информацию о любви.

        :return: Строка с информацией о любви

        Примеры:
        >>> love = Love("Анна", 12, 8.5)
        >>> love.display_info()
        'Партнёр: Анна, Длительность: 12, Интенсивность: 8.5'
        """
        return f"Партнёр: {self.partner}, Длительность: {self.duration}, Интенсивность: {self.intensity}"

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации

