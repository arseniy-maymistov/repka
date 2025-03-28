# Данные
disk_capacity_mb = 1.44
pages_in_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Переводим объем дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024

# Рассчитываем объем одной книги в байтах
book_size_bytes = pages_in_book * lines_per_page * chars_per_line * bytes_per_char

# Рассчитываем количество книг, которые можно разместить на дискете
number_of_books = disk_capacity_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(number_of_books))
