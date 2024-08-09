# First Django 2024

## Инструкция по развёртке:
1. `python3 -m venv django_venv`
2. `source django_venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`


## Запуск `ipython` в контексте приложений `django`
```
python manage.py shell_plus --ipython
```

## Для Visual Studio Code:
Установить расширение "Django" (автор "Baptiste Darthenay").

В settings прописать:
```
"emmet.includeLanguages": {
        "django-html": "html"
    },
"files.associations": {
    "*.html": "django-html"
}
```

