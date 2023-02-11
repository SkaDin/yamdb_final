![](https://github.com/SkaDin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# API для проекта YaMDB в Docker-контейнере

## Описание
### Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). Сайт не предоставляет прямой доступ или ссылки для непосредственного ознакомления с произведениями.

## Проект доступен по [Адресу](http://84.201.152.177/)
    Может быть недоступен в связи с прекращением обслуживания.
    
### Используемые технологии:
* Python 3.8 
* Django 3.2
* Django Rest Framework 3.12.4
* Docker 20.10.23
* CI и CD 


[![Python](https://www.python.org/)
## Как запустить проект:
### Все описанное ниже относится к ОС Linux и выполняется от имени администратора. Клонируем репозиторий и переходим в него:

```
git clone git@github.com:SkaDin/yamdb_final.git
```
### Выполнить вход на удаленный сервер и установить docker на сервер: 
```
apt install docker.io 
```
### Установить docker-compose на сервер:

```
curl -SL https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```
### Отредактировать и cкопировать файлы docker-compose.yml и nginx.conf из директории infra на сервер:

```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml

scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
### Добавить в Secrets GitHub переменные окружения для работы :
```
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>

DOCKER_PASSWORD=<пароль от DockerHub>
DOCKER_USERNAME=<имя пользователя>

SECRET_KEY=<секретный ключ проекта django>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<ID чата, в который придет сообщение>
TELEGRAM_TOKEN=<токен вашего бота>

```
### Workflow состоит из четырёх шагов:
1. Проверка кода на соответствие PEP8.
2. Сборка и отправка образа на DockerHub.
3. Автоматический деплой на удаленный сервер.
4. Отправка уведомления в телеграм-чат.

### После успешной сборки выполнить следующие действия (только при первом деплое):
### Провести миграцию внутри контейнера(собранного из образа):
```
docker-compose exec web python manage.py migrate
```
### Собираем статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
### Создаем суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
### Заполняем базу данными

### Создаем дамп базы данных (нет в текущем репозитории):
```
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```
### Останавливаем контейнеры:
```
docker-compose down -v
```
### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<секретный ключ проекта django>
```
### Основные используемые библиотеки:
```
asgiref==3.2.10
Django==2.2.16
django-filter==2.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.8.0
gunicorn==20.0.4
psycopg2-binary==2.8.6
PyJWT==2.1.0
pytz==2020.1
sqlparse==0.3.1 
```
## Автор проекта: 
SkaDin(Сушков Денис)

### Документация API YaMDb
```Документация доступна по эндпойнту: http://<IP-сервера>/redoc/ ```
