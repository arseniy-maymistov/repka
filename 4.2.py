# TODO решите задачу
import json
def task() -> float:
    # Чтение данных из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    # Проход по каждому словарю в списке
    for item in data:
        score = item.get("score", 0)  # Получаем значение по ключу "score"
        weight = item.get("weight", 0)  # Получаем значение по ключу "weight"

        # Вычисляем произведение и добавляем к общей сумме
        total_sum += score * weight

    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)


print(task())
