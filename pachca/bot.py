from client import HttpClient
from methods import BotMethods


class Bot:
    """
    Класс Бот.
    """

    def __init__(self, token=None):
        self.client = HttpClient(token)

    async def get_users(self):
        """
        Метод для получения списка пользователей.
        """
        return await BotMethods.get_users(self.client)

    async def get_user(self, id: int = None):
        """
        Метод для получения информации о пользователе.
        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_user_by_id(self.client, id=id)

    async def create_chat(self, chat: dict = None):
        """
        Метод для создания новой беседы или канала.
        Необходимые параметры:

        chat {
            name: str - Название
            member_ids: list[int] - Массив идентификаторов пользователей,
                                    которые станут участниками
            group_tag_ids: list[int] - Массив идентификаторов тегов,
                                       которые станут участниками
            channel: bool - Тип: беседа (по умолчанию, false) или канал (true)
            public: Доступ: закрытый (по умолчанию, false) или открытый (true)
        }

        """
        return await BotMethods.create_chat(self.client, chat)

    async def upload_file(self, file_path: str) -> str:
        """
        Метод для загрузки файла на сервер.

        Возвращает итоговый путь к файлу, который  будет использоваться для его
        прикрепления к сообщению и в других методах.

        Необходимые параметры:

        file_path: str - Абсолютный путь до загружаемого файла.

        """
        return await BotMethods.upload_file(self.client, file_path)

    async def send_message(self, message: dict) -> dict:
        """
        Метод для отправки сообщения.

        Необходимые параметры:

        message {
            entity_type: str - Тип сущности: беседа или канал (по умолчанию,
                               discussion),пользователь (user), тред (thread).
                               Для создания треда к сообщению воспользуйтесь
                               методом новый тред.
            entity_id: int - Идентификатор сущности.
            content: str - Текст сообщения.
            files [
                key: str - 	Путь к файлу, полученный в результате загрузки
                            файла (каждый файл в каждом сообщении должен
                            иметь свой уникальный key, не допускается
                            использование одного и того же key в разных
                            сообщениях).
                name: str - Название файла, которое вы хотите отображать
                            пользователю (рекомендуется писать вместе
                            с расширением).
                file_type: str - Тип файла: файл (file), изображение (image).
                size: int - Размер файла в байтах, отображаемый пользователю.
            ]
            parent_message_id: int - Идентификатор сообщения. Указывается в
                                     случае, если вы отправляете ответ
                                     на другое сообщение.
        }

        """
        return await BotMethods.send_messages(self.client, message)

    async def get_messages(
        self, chat_id: int, per: int = None, page: int = 1
    ) -> list[dict]:
        """
        Метод для получения списка сообщений.

        Возвращает список сообщений бесед, каналов, тредов и личных сообщений.

        Необходимые параметры:

        chat_id: int - Идентификатор чата (беседа, канал,
                       диалог или чат треда).
        per: int - Количество возвращаемых сущностей за один запрос
                   (по умолчанию 25, максимум 50).
        page: int - Страница выборки (по умолчанию 1).

        """
        return await BotMethods.get_messages(self.client, chat_id, per, page)

    async def get_message_by_id(self, id: int) -> dict:
        """
        Метод для получения информации о сообщении.

        Необходимые параметры:

        id: int - Идентификатор получаемого сообщения.

        """
        return await BotMethods.get_message_by_id(self.client, id)

    async def edit_message(self, id: int, message: dict) -> dict:
        """
        Метод для редактирования сообщения или комментария.

        Если массив files присылается пустым, то вложения сообщения
        (если они были) удаляются.

        Необходимые параметры:

        id: int - Идентификатор редактируемого сообщения.
        message {
            content: str - Текст сообщения.
            files [
                key: str - 	Путь к файлу, полученный в результате загрузки
                            файла (каждый файл в каждом сообщении должен
                            иметь свой уникальный key, не допускается
                            использование одного и того же key в разных
                            сообщениях).
                name: str - Название файла, которое вы хотите отображать
                            пользователю (рекомендуется писать вместе
                            с расширением).
                file_type: str - Тип файла: файл (file), изображение (image).
                size: int - Размер файла в байтах, отображаемый пользователю.
            ]
        }

        """
        return await BotMethods.edit_message(self.client, id, message)
