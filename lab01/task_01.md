# Задание № 1. Установка и настройка Git

Проверка установленной версии:

```bash
git --version
```

`git` запускает программу, а параметр `--version` просит вывести её версию.
В работе использован Git 2.53.0.

Настройка имени и электронной почты:

```bash
git config --global user.name "montana"
git config --global user.email "savenkoff.denis2016@gmail.com"
```

`config` изменяет настройки Git, а `--global` применяет их ко всем локальным
репозиториям пользователя. Поля `user.name` и `user.email` записываются в
каждый новый коммит.
