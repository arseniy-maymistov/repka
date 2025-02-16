class Car:
    """Базовый класс для автомобилей."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализация базового класса автомобиля.

        Args:
            make (str): Производитель автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
        """
        self._make = make  # Приватный атрибут для производителя автомобиля
        self._model = model  # Приватный атрибут для модели автомобиля
        self._year = year  # Приватный атрибут для года выпуска автомобиля

    @property
    def make(self) -> str:
        """Возвращает марку автомобиля."""
        return self._make

    @property
    def model(self) -> str:
        """Возвращает модель автомобиля."""
        return self._model

    @property
    def year(self) -> int:
        """Возвращает год выпуска автомобиля."""
        return self._year

    def drive(self) -> str:
        """Метод, описывающий движение автомобиля.

        Returns:
            str: Сообщение о том, что автомобиль движется.
        """
        return f"{self.make} {self.model} движется."

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает подготовленное для разработки представление объекта."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


class PassengerCar(Car):
    """Класс для легковых автомобилей, унаследованный от Car."""

    def __init__(self, make: str, model: str, year: int, passenger_capacity: int) -> None:
        """Инициализация легкового автомобиля.

        Args:
            make (str): Производитель автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            passenger_capacity (int): Вместимость по количеству пассажиров.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self._passenger_capacity = passenger_capacity  # Приватный атрибут для вместимости пассажиров

    @property
    def passenger_capacity(self) -> int:
        """Возвращает вместимость пассажиров автомобиля."""
        return self._passenger_capacity

    def drive(self) -> str:
        """Метод, описывающий движение легкового автомобиля.

        Returns:
            str: Сообщение о том, что легковой автомобиль движется с учетом вместимости пассажиров.
        """
        return f"{super().drive()} Вместимость: {self.passenger_capacity} пассажиров."

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()}, Вместимость: {self.passenger_capacity}"


class Truck(Car):
    """Класс для грузовых автомобилей, унаследованный от Car."""

    def __init__(self, make: str, model: str, year: int, cargo_capacity: float) -> None:
        """Инициализация грузового автомобиля.

        Args:
            make (str): Производитель автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            cargo_capacity (float): Вместимость по грузоподъемности в тоннах.
        """
        super().__init__(make, model, year)
        self._cargo_capacity = cargo_capacity  # Приватный атрибут для грузоподъемности

    @property
    def cargo_capacity(self) -> float:
        """Возвращает грузоподъемность грузового автомобиля."""
        return self._cargo_capacity

    def drive(self) -> str:
        """Метод, описывающий движение грузового автомобиля.

        Returns:
            str: Сообщение о том, что грузовой автомобиль движется с учетом грузоподъемности.
        """
        return f"{super().drive()} Грузоподъемность: {self.cargo_capacity} т."

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()}, Грузоподъемность: {self.cargo_capacity} т."


if __name__ == "__main__":
    # Примеры использования
    passenger_car = PassengerCar("Toyota", "Camry", 2021, 5)
    print(passenger_car)  # Вывод информации о легковом автомобиле
    print(passenger_car.drive())  # Методы для легкового автомобиля

    truck = Truck("MAN", "TGX", 2020, 18.0)
    print(truck)  # Вывод информации о грузовом автомобиле
    print(truck.drive())  # Методы для грузового автомобиля
