"""Задание № 2: добавить и проверить зависимость requests."""

# requests — внешняя библиотека, указанная в pyproject.toml и requirements.txt.
import requests


def requests_version() -> str:
    """Вернуть номер установленной версии библиотеки requests."""
    # Атрибут __version__ содержит версию импортированного пакета.
    return requests.__version__


def main() -> None:
    # Вызываем функцию и показываем, что зависимость успешно установлена.
    print(f"Установлена библиотека requests версии {requests_version()}")


if __name__ == "__main__":
    main()
