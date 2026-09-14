# Лабораторная работа № 1. Система контроля версий

Цель: научиться управлять версиями Python-проекта с помощью Git и GitHub.

В соответствии с заданием выполнены **все задания среднего уровня**:

1. Git установлен (`git --version`), имя и email настроены.
2. Создан локальный Git-репозиторий Python-проекта.
3. Добавлен `main.py`, создан коммит `feat(lab1): create Python project`.
4. Файл изменён, создан коммит `feat(lab1): update greeting`.
5. Создана ветка `feature`, в ней добавлен `feature.py`.
6. Ветка `feature` слита с `main` отдельным merge-коммитом.
7. Добавлен `.gitignore` для Python.
8. Локальный репозиторий связан с GitHub через `origin`.
9. Итоговые изменения отправлены в GitHub.
10. Репозиторий `octocat/Hello-World` клонирован, его история изучена и
    сохранена в `foreign_repository_history.txt`.

Проверить учебную историю можно командой:

```bash
git log --graph --oneline --decorate
```

Запуск файлов:

```bash
python lab01/main.py
python lab01/feature.py
```
