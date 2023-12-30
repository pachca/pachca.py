# Pachca.py
![](https://img.shields.io/badge/license-MIT-green) ![](https://img.shields.io/badge/python-3.12-blue)

- [Pachca.py](#pachcapy)
  - [Установка](#установка)
      - [PyPI](#pypi)
  - [Пример использования](#пример-использования)
  - [Методы](#методы)
    - [Беседы и каналы](#беседы-и-каналы)
    - [Cотрудники](#cотрудники)
    - [Теги](#теги)
    - [Загрузка файлов](#загрузка-файлов)
    - [Задачи](#задачи)
    - [Сообщения](#сообщения)
    - [Реакции](#реакции)
    - [Комментарии](#комментарии)

## Установка
#### PyPI
``` 
pip install -U package-name 
```

## Пример использования
``` python
import asyncio

from pachca import Bot

TOKEN = os.getenv('TOKEN')

async def main():
    bot = Bot(TOKEN)
    result = await bot.get_users()

if __name__ == '__main__':
    asyncio.run(main())
```

## Методы
### Беседы и каналы
  * **Список бесед и каналов**
    ``` python
    class Bot.get_chats(client: HttpClient)
    ```
    Метод для получение списка бесед и каналов по заданным параметрам.

  * **Информация о беседе или канале**
    ``` python
    class Bot.get_chat_by_id(client: HttpClient, id: int)
    ```
    Метод для получение информации о беседе или канале. Для получения беседы или канала вам необходимо знать её id и указать его в URL запроса.

  * **Новая беседа или канал**
    ``` python
    class Bot.create_chat(client: HttpClient, chat: dict)
    ```
    *Параметры:*
      * **chat**: 
        ``` python
        {
          "chat": {
              "name": str,
              "members_ids": list(int),
              "group_tag_ids": list(int),
              "channel": bool,
              "public": bool
            }
        }
        ```
    Метод для создания новой беседы или нового канала. При создании беседы или канала вы автоматически становитесь участником.

  * **Добавление пользователей**
    ``` python
    class Bot.add_members_to_chat(client: HttpClient, id: int, members_ids: dict)
    ```
    *Параметры:*
      * **members_ids**: 
        ``` python
        {
            "member_ids": list(int)
        }
        ```
    Метод для добавления пользователей в состав участников беседы или канала.

  * **Добавление тегов**
    ``` python
    class Bot.add_tags_to_chat(client: HttpClient, id: int, group_tag_ids: dict)
    ```
    *Параметры:*
      * **group_tag_ids**: 
        ``` python
        {
            "group_tag_ids": list(int)
        }
        ```
    Метод для добавления тегов в состав участников беседы или канала.

### Cотрудники
  * **Список сотрудников**
    ``` python
    class Bot.get_users(client: HttpClient)
    ```
    Метод для получения актуального списка сотрудников вашей компании.

  * **Информация о сотруднике**
    ``` python
    class Bot.get_user(client: HttpClient, id: int)
    ```
    Метод для получения информации о сотруднике. Для получения сотрудника вам необходимо знать его id.

### Теги
  * **Список тегов сотрудников**
    ``` python
    class Bot.get_group_tags(client: HttpClient)
    ```
    Метод для получения актуального списка тегов сотрудников. Названия тегов являются уникальными в компании

  * **Список сотрудников тега**
    ``` python
    class Bot.get_tag_users(client: HttpClient, tag_id: int)
    ```
    Метод для получения актуального списка сотрудников тега.
    
### Загрузка файлов
  * **Список сотрудников тега**
    ``` python
    class Bot.upload_file(client: HttpClient, file_path: str)
    ```
    Данный метод сперва выполняет запрос по адресу /uploads, чтобы получить необходимые парметры для загрузки файла. Затем, получив все параметры, выполняет запрос в форме multipart/form-data на адрес полученный ранее, оптравляя полученные параметры и сам файл.

### Задачи
  * **Новая задача**
    ``` python
    class Bot.create_task(client: HttpClient, task: dict)
    ```
    *Параметры:*
      * **task**: 
        ``` python
        {
          "task": {
              "kind": str,
              "content": str,
              "due_at": str,
              "priority": int,
              "performer_ids": list(int)
            }
        }
    Метод для создания новой задачи.

### Сообщения
  * **Новое сообщение**
    ``` python
    class Bot.send_message(client: HttpClient, message: dict)
    ```
    *Параметры:*
      * **message**: 
        ``` python
        {
          "message": {
              "entity_type": str,
              "entity_id": int,
              "content": str,
              "files": list(File),
              "parent_message_id": int
            }
        }
        ```
      * **File**: 
        ``` python
           {
                "key": str,
                "name": str,
                "file_type": str,
                "size": int
            }
        ```

    Метод для отправки сообщения в беседу или канал, личного сообщения пользователю или комментария в тред.

  * **Информация о сообщении**
    ``` python
    class Bot.get_message_by_id(client: HttpClient, id: int)
    ```
    Метод для отправки сообщения в беседу или канал, личного сообщения пользователю или комментария в тред.

  * **Список сообщений чата**
    ``` python
    class Bot.get_messages(client: HttpClient, chat_id: int, per: int, page: int)
    ```
    *Параметры:*
      * **chat_id:** Идентификатор чата
      * **per:** Количество возвращаемых сущностей за один запрос (по умолчанию 25, максимум 50)
      * **page:** Страница выборки (по умолчанию 1)
    Метод для отправки сообщения в беседу или канал, личного сообщения пользователю или комментария в тред.

  * **Редактирование сообщения**
    ``` python
    class Bot.edit_message(client: HttpClient, id: int, message: dict)
    ```
    *Параметры:*
      * **message**: 
        ``` python
        {
          "message": {
              "content": str,
              "files": list(File)
            }
        }
        ```
      * **File**: 
        ``` python
           {
                "key": str,
                "name": str,
                "file_type": str,
                "size": int
            }
        ```

    Метод для редактирования сообщения или комментария. Для редактирования сообщения вам необходимо знать его id. Все редактируемые параметры сообщения указываются в теле запроса.

### Реакции
  * **Добавление реакции**
    ``` python
    class Bot.add_reaction(client: HttpClient, id: int, data: dict)
    ```
    *Параметры:*
      * **data**: 
        ``` python
        {
          "code": str
        }
        ```
      * **File**: 
        ``` python
           {
                "key": str,
                "name": str,
                "file_type": str,
                "size": int
            }
        ```

    Метод для добавления реакции на сообщение. Для добавления реакции вам необходимо знать id сообщения.

  * **Удаление реакции**
    ``` python
    class Bot.delete_reaction(client: HttpClient, id: int)
    ```
    Метод для удаления реакции на сообщение. Для удаления реакции вам необходимо знать id сообщения.

  * **Список реакций**
    ``` python
    class Bot.get_reactions(client: HttpClient, id: int)
    ```
    Метод для получения актуального списка реакций на сообщение.

### Комментарии
  * **Новый тред**
    ``` python
    class Bot.create_thread(client: HttpClient, message_id: int)
    ```
    Метод для создания нового треда к сообщению.
