### Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории:«Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Картины» или «Ювелирные изделия»). Произведению может быть присвоен жанр из списка предустановленных (например, «Легенда», «Поп» или «Триллер»). Администратор может добавлять произведения, категории и жанры. 
Пользователи оставляют к произведениям отзывы и ставят произведению оценку в диапазоне от 1 до 10; из пользовательских оценок формируется рейтинг. Пользователь может оставить только один отзыв на одно произведение. Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Используемый стек:
Python 3.7, Django 3.2, DRF 3.12, DJOSER, PostgreSQL
### Как запустить проект:
Скачать и установить python 3.7 с сайта https://www.python.org/.

Зарегистрируйтесь на GitHub, при регистрации укажите имя пользователя, адрес электронной почты и придумайте пароль. После того как вы нажмёте кнопку «Создать аккаунт», система попросит вас подтвердить электронную почту. Загляните в почтовый ящик, там будет письмо с кодом подтверждения.

Скачайте и установите GitBash.
Запустите Git Bash (если у вас Windows) или Терминал (на Linux/MacOS). Выполните команду <code>ssh-keygen</code>
Консоль попросит ввести путь к файлу, в который будут сохранены сгенерированные ключи, и одновременно предложит сохранить их в файл по умолчанию:
<code>
Enter file in which to save the key (/home/имя_пользователя/.ssh/id_rsa):
</code>
Сохраните ключи в папку по умолчанию: для этого нажмите Enter на Windows или Return на macOS.
При создании ключей система попросит придумать пароль для доступа к ключам. Когда вы будете задавать пароль, в терминале ничего не отобразится, даже звёздочки.
Рисунок в окне терминала будет свидетельствовать, что ключи успешно созданы:
![](https://pictures.s3.yandex.net/resources/S0_8_1667171287.png)

Теперь необходимо сохранить открытый ключ в вашем аккаунте на GitHub. 
Выведите ключ в терминал командой:
<code> cat .ssh/id_rsa.pub </code>

Cкопируйте ключ от символов ssh-rsa , включительно, и до конца:

![](https://pictures.s3.yandex.net/resources/S0_9_1667171307.png)

Зайдите в свой аккаунт на GitHub, перейдите в раздел настроек.

Выберите пункт SSH and GPG keys; для создания нового ключа нажмите на кнопку New SSH key в правом верхнему углу.

Откроется страница с двумя полями ввода:
Title (заголовок ключа). Когда будете задавать заголовок, учитывайте, что в дальнейшем вы, возможно, добавите и другие ключи. Например, с другого своего компьютера, чтобы получить с него доступ к репозиториям на GitHub. Поэтому выбирайте для каждого ключа уникальные заголовки, например ключ с домашнего компьютера можно назвать HomePC, а с рабочего — WorkPC.
Key (ключ). Сюда необходимо вставить скопированный из терминала ключ.

Нажмите кнопку Add SSH key — ключ добавится к вашему аккаунту. Если вы захотите получить SSH-доступ к своему аккаунту на GitHub с нескольких компьютеров, для каждого из них должен быть создан и добавлен свой SSH-ключ.

Место, где хранится и обновляется код проекта, чаще всего в виде файлов, называют репозито́рием.

### Клонировать репозиторий и перейти в него в командной строке:
Напечатайте в терминале команду git clone, после неё поставьте пробел, вставьте скопированный адрес и выполните команду:

<code>git clone git@github.com:akiqq/foodgram-project-react.git</code>

### Запустить проект:

Перейти в foodgram-project-react/infra

docker-compose up -d --build

docker-compose exec backend python manage.py makemigrations

docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input

### Примеры запросов:

<br>POST http://localhost/api/auth/token/login/
<pre><code>
{
  "password": "1",
  "email": "a@k.ru"
}
</code></pre>

Пример ответа.
<pre><code>
{
    "auth_token": "a5df3685997c98c78d3c9e489bf720e7f9f3a84f"
}
</code></pre>

DELETE http://localhost/api/auth/token/logout/


GET http://localhost/api/users/<br>
<pre><code>
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/?page=4",
  "previous": "http://foodgram.example.org/api/users/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": false
    }
  ]
}
</code></pre>

POST http://127.0.0.1:8000/api/users/
<pre><code>
{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "Qwerty123"
}
</code></pre>

GET http://localhost/api/tags/
<pre><code>
[
  {
    "id": 0,
    "name": "Завтрак",
    "color": "#E26C2D",
    "slug": "breakfast"
  }
]
</code></pre>

GET http://127.0.0.1:8000/api/recipes/

Пример ответа.
<pre><code>
{
  "count": 123,
  "next": "http://foodgram.example.org/api/recipes/?page=4",
  "previous": "http://foodgram.example.org/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "user@example.com",
        "id": 0,
        "username": "string",
        "first_name": "Вася",
        "last_name": "Пупкин",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
</code></pre>

POST http://127.0.0.1:8000/api/recipes/
<pre><code>
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
</code></pre>

PATCH http://127.0.0.1:8000/api/v1/users/
<pre><code>
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
</code></pre>

Пример ответа.
<pre><code>
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "color": "#E26C2D",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": false
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "text": "string",
  "cooking_time": 1
}
</code></pre>

GET http://localhost/api/recipes/download_shopping_cart/

POST http://localhost/api/recipes/download_shopping_cart/
<pre><code>
{
  "id": 0,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "cooking_time": 1
}
</code></pre>

POST http://localhost/api/recipes/{id}/favorite/
<pre><code>
{
  "id": 0,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "cooking_time": 1
}
</code></pre>

GET http://localhost/api/users/subscriptions/
<pre><code>
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/subscriptions/?page=4",
  "previous": "http://foodgram.example.org/api/users/subscriptions/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": true,
      "recipes": [
        {
          "id": 0,
          "name": "string",
          "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
          "cooking_time": 1
        }
      ],
      "recipes_count": 0
    }
  ]
}
</code></pre>

GET http://localhost/api/ingredients/
<pre><code>
[
  {
    "id": 0,
    "name": "Капуста",
    "measurement_unit": "кг"
  }
]
</code></pre>

Автор: <br>[Александр](https://github.com/akiqq)
