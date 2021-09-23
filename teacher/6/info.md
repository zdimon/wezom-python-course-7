python3 -m venv venv
. ./venv/bin/activate
pip install pelican markdown
pelican-quickstart

В папке content index.md

    Title: My First Review
    Date: 2010-12-03 10:20
    Category: Review

    Following is a review of my favorite mechanical keyboard.

Собрать сайт 

    pelican content

Запускаем сервер

    pelican --listen




