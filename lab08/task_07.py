"""Задание № 7: использовать стандартный модуль logging."""

# logging записывает сообщения о работе программы.
import logging

# Получаем отдельный журнал с именем текущего файла.
logger = logging.getLogger(__name__)


def calculate_total(prices: list[float]) -> float:
    """Вычислить сумму цен и записать действия в журнал."""
    # Сообщаем, сколько элементов собираемся обработать.
    logger.info("Получено цен: %s", len(prices))
    # sum складывает все значения списка.
    total = sum(prices)
    # Записываем готовый результат.
    logger.info("Итоговая сумма: %s", total)
    # Возвращаем сумму вызывающему коду.
    return total


def main() -> None:
    # basicConfig включает показ сообщений уровня INFO и выше.
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    # Создаём список демонстрационных цен.
    prices = [120.0, 80.5, 49.5]
    # Вычисляем сумму; внутри функции появятся две записи журнала.
    total = calculate_total(prices)
    # Дополнительно показываем результат пользователю.
    print(f"Общая стоимость: {total}")


if __name__ == "__main__":
    main()
