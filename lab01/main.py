"""Лабораторная работа № 1: демонстрационный Python-проект."""


def greeting(name: str = "Git") -> str:
    """Вернуть персонализированное приветствие."""
    return f"Привет, {name}! Проект обновлён."


if __name__ == "__main__":
    print(greeting())
