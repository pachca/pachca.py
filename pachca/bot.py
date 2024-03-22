from pachca.client import HttpClient
from pachca.methods import BotMethods


class Bot:
    """
    Класс Бот.
    """

    def __init__(self, token):
        self.client = HttpClient(token)

    async def get_users(self, *args, **kwargs):
        """
        Метод для получения списка пользователей.
        """
        kwargs['client'] = self.client
        return await BotMethods.get_users(*args, **kwargs)

    async def get_user(self, *args, id: int, **kwargs):
        """
        Метод для получения информации о пользователе.

        Необходимые параметры:

        id: int

        """
        kwargs['client'] = self.client
        return await BotMethods.get_user_by_id(*args, id=id, **kwargs)

    async def get_group_tags(self, *args, **kwargs):
        """
        Метод для получения актуального списка тегов сотрудников.
        Названия тегов являются уникальными в компании.
        """
        kwargs['client'] = self.client
        return await BotMethods.get_group_tags(*args, **kwargs)

    async def get_tag_users(self, *args, tag_id: int, **kwargs):
        """
        Метод для получения актуального списка сотрудников тега.
        Необходимые параметы:

        tag_id: int
        """
        kwargs['client'] = self.client
        return await BotMethods.get_group_tag_users(*args, tag_id=tag_id, **kwargs)

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
            files: list - [
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

    async def get_chats(self):
        """
        Метод для получение списка бесед и каналов.
        """
        return await BotMethods.get_chats(self.client)

    async def get_chat_by_id(self, id: int = None):
        """
        Метод для получение информации о беседе или канале.
        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_chat_by_id(self.client, id=id)

    async def create_chat(self, *args, **kwargs):
        """
        Метод для создания новой беседы или канала.
        Необходимые параметры:

        **kwargs:
        name: str - Название
        member_ids: list[int] - Массив идентификаторов пользователей,
                                которые станут участниками
        group_tag_ids: list[int] - Массив идентификаторов тегов,
                                   которые станут участниками
        channel: bool - Тип: беседа (по умолчанию, false) или канал (true)
        public: bool - Доступ: закрытый (по умолчанию, false) или открытый
        (true)
        """
        return await BotMethods.create_chat(self.client, **kwargs)

    async def add_members_to_chat(
            self,
            id: int = None,
            member_ids: dict = None
    ):
        """
        Метод для добавления пользователей в состав участников
        беседы или канала.
        Необходимые параметры:

        member_ids: list[int] - Массив идентификаторов пользователей,
                                    которые станут участниками

        """
        return await BotMethods.add_members_to_chat(
            self.client,
            id,
            member_ids
        )

    async def add_tags_to_chat(
            self,
            id: int = None,
            group_tag_ids: dict = None
    ):
        """
        Метод для добавления тегов в состав участников беседы или канала.
        Необходимые параметры:

        group_tag_ids: list[int] - Массив идентификаторов тегов,
                                    которые станут участниками

        """
        return await BotMethods.add_tags_to_chat(
            self.client,
            id,
            group_tag_ids
        )

    async def add_reaction(self, message_id, data):
        """
        Метод для добавления реакции на сообщение.
        Для добавления реакции вам необходимо знать id сообщения.
        """
        return await BotMethods.add_reaction(self.client,
                                             id=message_id, data=data)

    async def create_task(self, task: dict):
        """
        Метод для создания новой задачи.
        """
        return await BotMethods.create_task(self.client, task)

    async def get_reactions(self, message_id: int):
        """
        Метод для получения актуального списка реакций на сообщение.

        Необходимые параметры:

        message_id: int

        """
        return await BotMethods.get_reactions(message_id, self.client)

    async def delete_reaction(self, message_id: int, reaction: dict):
        """
        Метод для удаления реакции на сообщение.

        Необходимые параметры:

        {code: str - Emoji символ реакции}

        """
        return await BotMethods.delete_reaction(
            message_id, self.client, reaction
        )

    async def create_thread(self, message_id: int):
        """
        Метод для создания нового треда к сообщению.

        Необходимые параметры:

        message_id: int

        """
        return await BotMethods.create_thread(message_id, self.client)
