from pachca.client import HttpClient, MessagesData, ChatData, File, FileType
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
        return await BotMethods.get_users(*args, client=self.client, **kwargs)

    async def get_user(self, *args, id: int, **kwargs):
        """
        Метод для получения информации о пользователе.

        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_user_by_id(*args, client=self.client, id=id, **kwargs)

    async def get_group_tags(self, *args, **kwargs):
        """
        Метод для получения актуального списка тегов сотрудников.
        Названия тегов являются уникальными в компании.
        """
        return await BotMethods.get_group_tags(*args, client=self.client, **kwargs)

    async def get_tag_users(self, *args, tag_id: int, **kwargs):
        """
        Метод для получения актуального списка сотрудников тега.
        Необходимые параметы:

        tag_id: int
        """
        return await BotMethods.get_group_tag_users(*args, client=self.client, tag_id=tag_id, **kwargs)

    async def upload_file(self, file_path: str, file_type: FileType) -> str:
        """
        Метод для загрузки файла на сервер.

        Возвращает итоговый файл, который будет использоваться для
        прикрепления к сообщению и в других методах.

        Необходимые параметры:

        file_path: str - Абсолютный путь до загружаемого файла.
        file_type: FileType - Тип файла: файл (file), изображение (image).

        """
        return await BotMethods.upload_file(self.client, file_path, file_type)

    async def send_message(
            self, *args, entity_id: int, content: str, entity_type: str = None,
            files: File = None, parent_message_id: int = None, **kwargs
    ) -> dict:
        """
        Метод для отправки сообщения.

        Необходимые параметры:

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

        """
        if len(str(content)) < 1:
            raise ValueError('Сообщение не может быть пустым!')
        if entity_id is None:
            raise ValueError('Необходимо указать "entity_id"!')
        message_data = MessagesData(
            entity_type=entity_type,
            entity_id=entity_id,
            content=content,
            files=files,
            parent_message_id=parent_message_id,
        )
        message = {'message': message_data}
        return await BotMethods.send_messages(*args, client=self.client, message=message, **kwargs)

    async def get_messages(
        self, *args, chat_id: int, per: int = None, page: int = 1, **kwargs
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
        return await BotMethods.get_messages(*args, client=self.client, chat_id=chat_id, per=per, page=page, **kwargs)

    async def get_message_by_id(self, *args, id: int, **kwargs) -> dict:
        """
        Метод для получения информации о сообщении.

        Необходимые параметры:

        id: int - Идентификатор получаемого сообщения.

        """
        return await BotMethods.get_message_by_id(*args, client=self.client, id=id, **kwargs)

    async def edit_message(self, *args, id: int, content: str, files: File = None, **kwargs) -> dict:
        """
        Метод для редактирования сообщения или комментария.

        Если массив files присылается пустым, то вложения сообщения
        (если они были) удаляются.

        Необходимые параметры:

        id: int - Идентификатор редактируемого сообщения.

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

        """
        if files is None:
            files = []
        message_data = MessagesData(
            content=content,
            files=files,
        )
        message = {'message': message_data}
        return await BotMethods.edit_message(*args, client=self.client, id=id, message=message, **kwargs)

    async def get_chats(self, *args, **kwargs):
        """
        Метод для получение списка бесед и каналов.
        """
        return await BotMethods.get_chats(*args, client=self.client, **kwargs)

    async def get_chat_by_id(self, *args, id: int = None, **kwargs):
        """
        Метод для получение информации о беседе или канале.
        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_chat_by_id(*args, client=self.client, id=id, **kwargs)

    async def create_chat(self, *args, name: str, member_ids: list[int] = None,
                          group_tag_ids: list[int] = None, channel: bool = False, public: bool = False, **kwargs):
        """
        Метод для создания новой беседы или канала.
        Необходимые параметры:

        name: str - Название
        member_ids: list[int] - Массив идентификаторов пользователей,
                                которые станут участниками
        group_tag_ids: list[int] - Массив идентификаторов тегов,
                                   которые станут участниками
        channel: bool - Тип: беседа (по умолчанию, false) или канал (true)
        public: bool - Доступ: закрытый (по умолчанию, false) или открытый
        (true)
        """
        chat = ChatData(
            name=name,
            member_ids=member_ids,
            group_tag_ids=group_tag_ids,
            channel=channel,
            public=public,
        )
        chat_data = {'chat': chat}
        return await BotMethods.create_chat(*args, client=self.client, chat=chat_data, **kwargs)

    async def add_members_to_chat(
            self,
            *args,
            id: int,
            member_ids: list[int],
            silent: bool = False,
            **kwargs,
    ):
        """
        Метод для добавления пользователей в состав участников
        беседы или канала.
        Необходимые параметры:

        id: int - Уникальный id беседы или канала.
        member_ids: list[int] - Массив идентификаторов пользователей, которые станут участниками.
        silent: bool - 	Cоздавать в чате системное сообщение о добавлении участника, по умолчанию нет (False).

        """
        return await BotMethods.add_members_to_chat(
            *args,
            client=self.client,
            id=id,
            member_ids=member_ids,
            silent=silent,
            **kwargs,
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
