"""Задание № 2: класс «Студент» с методом вывода информации."""


class Student:
    """Хранить имя, возраст и группу студента."""

    def __init__(self, name: str, age: int, group: str) -> None:
        # self.name сохраняет имя внутри созданного объекта.
        self.name = name
        # self.age сохраняет возраст.
        self.age = age
        # self.group сохраняет название учебной группы.
        self.group = group

    def get_info(self) -> str:
        """Собрать информацию о студенте в одну строку."""
        # f-строка подставляет значения полей объекта в текст.
        return f"Студент: {self.name}; возраст: {self.age}; группа: {self.group}"

    def show_info(self) -> None:
        """Вывести информацию о студенте на экран."""
        # Метод print выводит строку, которую вернул get_info.
        print(self.get_info())


def main() -> None:
    # Создаём объект класса Student и передаём ему данные.
    student = Student("Анна", 20, "ПИ-21")
    # Вызываем метод вывода информации.
    student.show_info()


if __name__ == "__main__":
    main()
