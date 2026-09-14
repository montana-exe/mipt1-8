# Задание № 10. Клонирование чужого репозитория

Для изучения выбран небольшой публичный репозиторий GitHub:

```bash
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
git log --oneline --graph --all
```

`git clone` загружает файлы и всю доступную историю. `git log` показывает
коммиты, `--oneline` сокращает каждую запись до одной строки, `--graph`
рисует схему веток, а `--all` включает все ветки. Результат изучения сохранён
в `foreign_repository_history.txt`.
