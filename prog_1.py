import doctest
class LibraryItem:
    """
    Абстрактный класс, представляющий предмет библиотеки.

    Attributes:
        title (str): Название предмета.
        author (str): Автор предмета.
        year (int): Год выпуска предмета.
        is_checked_out (bool): Статус наличия предмета в библиотеке.
    """

    def __init__(self, title: str, author: str, year: int):
        if year < 1440 or year > 2023:  # Проверка на допустимый год выпуска
            raise ValueError("Год выпуска должен быть между 1440 и 2023.")
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False

    def check_out(self) -> None:
        """Выдает предмет на руки."""
        ...


    def return_item(self) -> None:
        """Возвращает предмет в библиотеку."""
        ...


class Book(LibraryItem):
    """
    Класс, представляющий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год выпуска книги.
    """

    def check_out(self) -> None:
        if self.is_checked_out:
            raise Exception("Книга уже выдана.")
        self.is_checked_out = True
        print(f"Книга '{self.title}' выдана.")

    def return_item(self) -> None:
        if not self.is_checked_out:
            raise Exception("Книга не была выдана.")
        self.is_checked_out = False
        print(f"Книга '{self.title}' возвращена.")


class Reader:
    """
    Класс, представляющий читателя библиотеки.

    Attributes:
        name (str): Имя читателя.
        borrowed_items (List[LibraryItem]): Список выданных предметов.
    """

    def __init__(self, name: str):
        self.name = name
        self.borrowed_items: List[LibraryItem] = []

    def borrow_item(self, item: LibraryItem) -> None:
        """Выдает предмет читателю."""
        item.check_out()
        self.borrowed_items.append(item)

    def return_item(self, item: LibraryItem) -> None:
        """Возвращает предмет читателем."""
        item.return_item()
        self.borrowed_items.remove(item)


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
