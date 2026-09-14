# Задание № 6. Слияние ветки feature с основной

```bash
git switch main
git merge --no-ff feature -m "merge: integrate feature branch"
```

Первая команда возвращает нас в основную ветку `main`. `git merge` переносит
изменения из `feature`. Параметр `--no-ff` создаёт отдельный merge-коммит,
поэтому слияние хорошо видно на графике истории. Его идентификатор — `88529db`.
