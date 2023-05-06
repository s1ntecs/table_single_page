## Начало работы

### Как запустить проект:


Клонировать GitHub репозиторий:

```
git clone https://github.com/s1ntecs/table_single_page.git

```

```
Необходимо создать файл переменных окружения .env .
Образец заполнения файла можете посмотреть в example.env.

```
После создания файла .env:

```
  - docker-compose up -d --build 

```

Теперь в контейнере web нужно выполнить миграции, создать суперпользователя и собрать статику:

```
docker-compose exec web python manage.py migrate

```


Соберем Статику:

```
docker-compose exec web python manage.py collectstatic --no-input

```

Запустим скрипт для случайных создания данных:

```
docker-compose exec web python manage.py populate_data

```
заходите по ссылке:
http://localhost/table/
