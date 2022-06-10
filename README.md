# django-orm-watching-storage

Скрипт представляет собой пульт охраны и банка. Показывает кто сейчас в хранилище с деньгами, сколько раз сотрудники ходили в хранилище, а если кто-то украл деньги — с кем он там был

## Добавление переменных окружения в скрипт
Для работы со скриптами Вам необходимо будет создать и настройть файл с переменными окуржения `.env`.

Для работы со скриптом `manage.py` в файл  `settings.py` необходимо передать перемнные окружения. Для этого в файл `.env` передаем следующие данные
- `USER`
- `PASSWORD`
- `SECRET_KEY`


Пример переданных данных для скрипта 
- `USER = guard`
- `PASSWORD = osim5`
- `SECRET_KEY = REPLACE_ME`


## Запуск скрипта 
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
`pip install -r requirements.txt`

Для запуска скрипта `manage.py`, пропишите в командной строке `python manage.py runserver 0.0.0.0:8000` и скрипт запустит локальный сайт .

## Пример запуска скриптов 
 `\Alex K\p_p\django-orm-watching-storage> python manage.py runserver 0.0.0.0:8000`
***
 

