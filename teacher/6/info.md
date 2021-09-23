python3 -m venv venv
. ./venv/bin/activate
pip install pelican markdown
pelican-quickstart

В папке content index.md

    Title: My First Review
    Date: 2010-12-03 10:20
    Category: Review

    Following is a review of my favorite 
    mechanical keyboard.
    # Заголовок
    ## Поменьше заголовок
    [ссылка](http://google.com)
    ![картинка](http://google.com)



Собрать сайт 

    pelican content

Запускаем сервер

    pelican --listen

Берем шаблоны

    git clone git@github.com:getpelican/pelican-themes.git

Прописываем шаблон в pelicanconf.py

    THEME = "pelican-themes/bootstrap"

# Джанго

    pip install Django

Создание проекта

    django-admin startproject blog

Создание БД

    cd blog
    ./manage.py migrate

Создание пользователя

    ./manage.py createsuperuser

Запуск сервера

    ./manage.py runserver 0.0.0.0:8000

