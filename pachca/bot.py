from client import HttpClient
from methods import BotMethods


class Bot:
    """
    Класс Бот.
    """

    def __init__(self, token):
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

        id - Идентификатор пользователя.
        """
        return await BotMethods.get_user_by_id(self.client, id=id)

    async def get_group_tags(self):
        """
        Метод для получения актуального списка тегов сотрудников.
        Названия тегов являются уникальными в компании.
        """
        return await BotMethods.get_group_tags(self.client)

    async def get_tag_users(self, tag_id: int = None):
        """
        Метод для получения актуального списка сотрудников тега.
        Необходимые параметы:

        tag_id - Идентификатор тега.
        """
        return await BotMethods.get_group_tag_users(self.client, tag_id=tag_id)

    async def create_chat(
            self,
            name: str = None,
            member_ids: list[int] = None,
            group_tag_ids: list[int] = None,
            channel: bool = False,
            public: bool = False
    ):
        """
        Метод для создания новой беседы или канала.
        Необходимые параметры:

        name - Название
        member_ids - Массив идентификаторов пользователей,
                                которые станут участниками
        group_tag_ids - Массив идентификаторов тегов,
                                    которые станут участниками
        channel - Тип: беседа (по умолчанию, false)
        public - Доступ: закрытый (по умолчанию, false)
        """
        return await BotMethods.create_chat(
            self.client, name, member_ids, group_tag_ids, channel, public)

    async def get_chat_by_id(self, id: int = None):
        """
        Метод для получение информации о беседе или канале.
        Необходимые параметры:

        id - Идентификатор чата.
        """
        return await BotMethods.get_chat_by_id(self.client, id=id)

    async def get_chats(self):
        """
        Метод для получение списка бесед и каналов.
        """
        return await BotMethods.get_chats(self.client)

    async def add_members_to_chat(
            self,
            id: int = None,
            member_ids: list = None,
            silent: bool = False
    ):
        """
        Метод для добавления пользователей в состав участников
        беседы или канала.
        Необходимые параметры:

        member_ids - Массив идентификаторов пользователей,
                     которые станут участниками
        silent - Не создавать в чате системное сообщение о добавлении участника
        """
        return await BotMethods.add_members_to_chat(
            self.client, id, member_ids, silent)

    async def add_tags_to_chat(
            self,
            id: int = None,
            group_tag_ids: list = None
    ):
        """
        Метод для добавления тегов в состав участников беседы или канала.
        Необходимые параметры:

        group_tag_ids - Массив идентификаторов тегов,
                        которые станут участниками
        """
        return await BotMethods.add_tags_to_chat(
            self.client, id, group_tag_ids)

    async def create_thread(self, message_id: int):
        """
        Метод для создания нового треда к сообщению.
        Необходимые параметры:

        message_id - Идентификатор сообщения.
        """
        return await BotMethods.create_thread(message_id, self.client)

    async def send_message(
            self,
            entity_type: str = None,
            entity_id: int = None,
            content: str = None,
            files: list[dict] = None,
            parent_message_id: int = None
    ):
        """
        Метод для отправки сообщения.
        Необходимые параметры:

        entity_type - Тип сущности: беседа или канал (по умолчанию,
                      discussion),пользователь (user), тред (thread).
                      Для создания треда к сообщению воспользуйтесь
                      методом новый тред.
        entity_id - Идентификатор сущности.
        content - Текст сообщения.
        files: {
            name - Название файла, которое вы хотите отображать
                   пользователю (рекомендуется писать вместе
                   с расширением).
            file_type - Тип файла: файл (file), изображение (image).
            size - Размер файла в байтах, отображаемый пользователю.
            file_path - Путь до файла.
        }
        parent_message_id - Идентификатор сообщения. Указывается в
                            случае, если вы отправляете ответ
                            на другое сообщение.
        """
        if files is not None:
            for file in files:
                file['key'] = await BotMethods.upload_file(
                    self.client, file_path=file.pop('file_path'))
        return await BotMethods.send_messages(
            self.client, entity_type, entity_id,
            content, files, parent_message_id
        )

    async def get_message_by_id(self, id: int = None):
        """
        Метод для получения информации о сообщении.
        Необходимые параметры:

        id - Идентификатор получаемого сообщения.
        """
        return await BotMethods.get_message_by_id(self.client, id)

    async def get_messages(
        self, chat_id: int = None, per: int = None, page: int = 1
    ):
        """
        Метод для получения списка сообщений.
        Возвращает список сообщений бесед, каналов, тредов и личных сообщений.
        Необходимые параметры:

        chat_id - Идентификатор чата (беседа, канал,
                  диалог или чат треда).
        per - Количество возвращаемых сущностей за один запрос
              (по умолчанию 25, максимум 50).
        page - Страница выборки (по умолчанию 1).
        """
        return await BotMethods.get_messages(self.client, chat_id, per, page)

    async def edit_message(
        self,
        id: int = None,
        content: str = None,
        files: dict = None,
    ):
        """
        Метод для редактирования сообщения или комментария.
        Если массив files присылается пустым, то вложения сообщения
        (если они были) удаляются.
        Необходимые параметры:

        id - Идентификатор редактируемого сообщения.
        content - Текст сообщения.
        files: {
            key - Путь к файлу, полученный в результате загрузки
                  файла (каждый файл в каждом сообщении должен
                  иметь свой уникальный key, не допускается
                  использование одного и того же key в разных
                  сообщениях).
            name - Название файла, которое вы хотите отображать
                   пользователю (рекомендуется писать вместе
                   с расширением).
            file_type - Тип файла: файл (file), изображение (image).
            size - Размер файла в байтах, отображаемый пользователю.
        }
        """
        if files is not None:
            for file in files:
                file['key'] = await BotMethods.upload_file()
        return await BotMethods.edit_message(
            self.client, id, content, files)

    async def add_reaction(
            self,
            message_id: int = None,
            code: str = None
    ):
        """
        Метод для добавления реакции на сообщение.
        """
        return await BotMethods.add_reaction(
            self.client, message_id=message_id, code=code)

    # В документации Пачки, неправильно указан URL для этого эндпоинта
    #
    # async def get_reactions(
    #     self, per: int = None, page: int = 1
    # ):
    #     """
    #     Метод для получения актуального списка реакций.
    #     Необходимые параметры:

    #     per - Количество возвращаемых сущностей за один запрос
    #           (по умолчанию 25, максимум 50).
    #     page - Страница выборки (по умолчанию 1).
    #     """
    #     return await BotMethods.get_reactions(self.client, per, page)

    async def delete_reaction(
            self, message_id: int = None, code: str = None):
        """
        Метод для удаления реакции на сообщение.
        Необходимые параметры:

        code - Emoji символ реакции
        """
        return await BotMethods.delete_reaction(
            self.client, message_id=message_id, code=code
        )

    async def delete_reaction(self, message_id: int = None, code: str = None):
        """
        Метод для удаления реакции на сообщение.
        Необходимые параметры:

        code - Emoji символ реакции
        """
        return await BotMethods.delete_reaction(
            self.client, message_id=message_id, code=code
        )

    async def create_task(
            self,
            kind: str = None,
            content: str = None,
            due_at: str = None,
            priority: int = None,
            performer_ids: list[int] = None
    ):
        """
        Метод для создания новой задачи.

        kind - Тип: call (позвонить контакту), meeting (встреча),
               reminder (напоминание), event (событие), email (написать письмо)
        content	- Описание (по умолчанию - название типа)
        due_at - Срок выполнения задачи (ISO-8601) в формате
                 YYYY-MM-DDThh:mm:ss.sssTZD. Если указано время 23:59:59.000,
                 то задача будет создана на весь день (без указания времени).
        priority - Приоритет: 1 (по умолчанию), 2 (важно) или 3 (очень важно).
        performer_ids - Массив идентификаторов пользователей, привязываемых к
                        задаче как «ответственные» (по умолчанию ответственным
                        назначаетесь вы)
        """
        return await BotMethods.create_task(
            self.client, kind, content, due_at, priority, performer_ids)
