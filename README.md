## API_YAMDB
#### REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке.

### Описание
#### Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

#### Используемые технологии:
* Python 3.8
* Django 3.2
* Django Rest Framework 3.12.4
* Docker 20.10.23

### Как запустить проект:
#### Все описанное ниже относится к ОС Linux. Клонируем репозиторий и переходим в него:

```
git clone git@github.com:SkaDin/infra_sp2.git
```
```
cd infra_sp2
cd api_yamdb
```
#### Создаем и активируем виртуальное окружение:
```
python3 -m venv venv
. /venv/bin/activate
python -m pip install --upgrade pip
```
#### Устанавливаем зависимости из requirements.txt:

```
pip install -r requirements.txt
```
#### Переходим в папку с файлом docker-compose.yaml:

```
cd infra
```
#### Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):
```
docker-compose up -d --build
```
#### Выполняем миграции:
```
docker-compose exec web python manage.py migrate
```
```
docker-compose exec web python manage.py migrate --run-syncdb
```
#### Собираем статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
#### Создаем суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
#### Создаем дамп базы данных (нет в текущем репозитории):
```
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```
#### Останавливаем контейнеры:
```
docker-compose down -v
```
#### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
#### Основные используемые библиотеки:
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
### Автор проекта: 
SkaDin(Сушков Денис)

#### Документация API YaMDb
```Документация доступна по эндпойнту: http://localhost/redoc/ ```
