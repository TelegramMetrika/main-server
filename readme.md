<h1 align="center">
	<img src="https://raw.githubusercontent.com/TelegramMetrika/main-server/main/imgs/1024.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/dev/assets/misc/transparent.png" height="30" width="0px"/>
	TelegramMetrika
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/dev/assets/misc/transparent.png" height="30" width="0px"/>
</h1>
<h3 align="center">метрика для Телеграм ботов</h3>

## В разработке применяется ##

* [Python 3.10](https://www.python.org/) - язык программирования

* [FastAPI](https://fastapi.tiangolo.com) - основной фреймворк

* [SQLObject](http://sqlobject.org) - ORM для работы с базой данный

* [Pydantic](https://pydantic-docs.helpmanual.io) - валидация данных

## Описание репозитория ##

* /mod
  * api.py - ресурсы сервера с psutil
  * db.py - подключение к БД
  * model.py - модели классов для БД и запросов
  * post.py - функции работы с БД
  * error.py - описание ошибок на русском
  * utils.py - функции преобразования
* app.py - основной код сервера
* create_db.py - создание БД

## Описание API ##

* Для запросов необходим токен, который можно получить /create/, пример json запроса(в ответ будет получен токен):

```
{
  "bot_id": 1234567,
  "name": "Обратная связь",
  "username": "@usernameBot"
}
```

* Чтобы получить(/get/) или добавить(/add/) данные метрики надо будет использовать токен заголовком запроса "Authorization", отправка данных:

```
{
  "user": {
    ...
  }
}
```

## Лицензия ##

Copyright (c) 2022 - настоящее время, главный разработчик - [vsecoder](https://github.com/vsecoder).

TelegramMetrika находится под лицензией MIT.