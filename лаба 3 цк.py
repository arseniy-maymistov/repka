class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используется свойство для проверки значений

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используется свойство для проверки значений

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self.duration} часов"


# Примеры использования
paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
print(paper_book)  # Книга '1984'. Автор: Джордж Оруэлл, Количество страниц: 328
print(repr(paper_book))  # PaperBook(name='1984', author='Джордж Оруэлл')

audio_book = AudioBook("Гарри Поттер и философский камень", "Джоан Роулинг", 8.5)
print(audio_book)  # Книга 'Гарри Поттер и философский камень'. Автор: Джоан Роулинг, Продолжительность: 8.5 часов
print(repr(audio_book))  # AudioBook(name='Гарри Поттер и философский камень', author='Джоан Роулинг')
