from pachca.client import HttpClient, MessagesData, ChatData, TaskData, File, FileType, UserData, CustomProperties

from pachca.methods import BotMethods


class Bot:
    """
    Класс Бот.
    """

    def __init__(self, token):
        self.client = HttpClient(token)

    async def get_users(self, *args, **kwargs) -> dict:
        """
        Метод для получения списка пользователей.
        """
        return await BotMethods.get_users(*args, client=self.client, **kwargs)

    async def get_user(self, *args, id: int, **kwargs) -> dict:
        """
        Метод для получения информации о пользователе.

        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_user_by_id(*args, client=self.client, id=id, **kwargs)

    async def create_user(
        self,
        *args,
        email,
        first_name=None,
        last_name=None,
        nickname=None,
        phone_number=None,
        department=None,
        role=None,
        suspended=None,
        list_tags=None,
        custom_properties: CustomProperties = None,
        skip_email_notify=None,
        **kwargs,
    ) -> dict:
        """
        Метод для создания нового сотрудника в вашей компании.


        """
        user_data = UserData(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            email=email,
            phone_number=phone_number,
            department=department,
            role=role,
            suspended=suspended,
            list_tags=list_tags,
            custom_properties=custom_properties,
            skip_email_notify=skip_email_notify,
        )
        return await BotMethods.create_user(*args, client=self.client, user_data=user_data, **kwargs)

    async def edit_user(
        self,
        *args,
        email=None,
        first_name=None,
        last_name=None,
        nickname=None,
        phone_number=None,
        department=None,
        role=None,
        suspended=None,
        list_tags=None,
        custom_properties=None,
        skip_email_notify=None,
        **kwargs,
    ) -> dict:
        """
        Метод для редактирования сотрудника.
        """
        user_data = UserData(
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            email=email,
            phone_number=phone_number,
            department=department,
            role=role,
            suspended=suspended,
            list_tags=list_tags,
            custom_properties=custom_properties,
            skip_email_notify=skip_email_notify,
        )
        return await BotMethods.edit_user(*args, client=self.client, user_data=user_data, **kwargs)

    async def delete_user(self, *args, id, **kwargs) -> dict:
        """
        Метод для удаления сотрудника.
        """
        return await BotMethods.delete_user(*args, client=self.client, id=id, **kwargs)

    async def get_group_tags(self, *args, **kwargs) -> dict:
        """
        Метод для получения актуального списка тегов сотрудников.
        Названия тегов являются уникальными в компании.
        """
        return await BotMethods.get_group_tags(*args, client=self.client, **kwargs)

    async def get_tag_users(self, *args, tag_id: int, **kwargs) -> dict:
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

    async def custom_properties(self, entity_type: str) -> str:
        """
        Метод для получения актуального списка
        дополнительных полей сотрудников в вашей компании.

        Необходимые параметры:

        entity_type: str - Тип сущности: сотрудник (user).
        """
        return await BotMethods.get_custom_properties(self.client, entity_type)

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
        return await BotMethods.send_messages(*args, client=self.client, message_data=message_data, **kwargs)

    async def get_messages(
        self, *args, chat_id: int, per: int = None, page: int = 1, **kwargs
    ) -> dict:
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
        return await BotMethods.edit_message(*args, client=self.client, id=id, message_data=message_data, **kwargs)

    async def get_chats(self, *args, **kwargs) -> dict:
        """
        Метод для получение списка бесед и каналов.
        """
        return await BotMethods.get_chats(*args, client=self.client, **kwargs)

    async def get_chat_by_id(self, *args, id: int = None, **kwargs) -> dict:
        """
        Метод для получение информации о беседе или канале.
        Необходимые параметры:

        id: int - Идентификатор беседы или канала

        """
        return await BotMethods.get_chat_by_id(*args, client=self.client, id=id, **kwargs)

    async def create_chat(self, *args, name: str, member_ids: list[int] = None,
                          group_tag_ids: list[int] = None, channel: bool = False, public: bool = False, **kwargs) -> dict:
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
        chat_data = ChatData(
            name=name,
            member_ids=member_ids,
            group_tag_ids=group_tag_ids,
            channel=channel,
            public=public,
        )
        return await BotMethods.create_chat(*args, client=self.client, chat_data=chat_data, **kwargs)

    async def update_chat(self, *args, id: int, name: str = None, public: bool = None, **kwargs) -> dict:
        """
        Метод для создания новой беседы или канала.
        Необходимые параметры:

        id: int - идентификатор беседы или канала.

        name: str - Название
        public: bool - Доступ: закрытый (по умолчанию, false) или открытый (true)
        """
        if name is None and public is None:
            raise AttributeError('Обязательно наличие хотя бы одного из параметров: name или public')
        chat_data = ChatData(
            name=name,
            public=public,
        )
        return await BotMethods.update_chat(*args, client=self.client, id=id, chat_data=chat_data, **kwargs)

    async def add_members_to_chat(
            self,
            *args,
            id: int,
            member_ids: list[int],
            silent: bool = False,
            **kwargs,
    ) -> None:
        """
        Метод для добавления пользователей в состав участников
        беседы или канала.
        Необходимые параметры:

        id: int - Уникальный id беседы или канала.
        member_ids: list[int] - Массив идентификаторов пользователей, которые станут участниками.
        silent: bool - 	Cоздавать в чате системное сообщение о добавлении участника, по умолчанию - нет (False).

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
            *args,
            id: int = None,
            group_tag_ids: list[int] = None,
            **kwargs,
    ) -> None:
        """
        Метод для добавления тегов в состав участников беседы или канала.
        Необходимые параметры:

        id: int - Идентификатор беседы/канала.
        group_tag_ids: list[int] - Массив идентификаторов тегов, которые станут участниками.

        """
        return await BotMethods.add_tags_to_chat(
            *args,
            client=self.client,
            id=id,
            group_tag_ids=group_tag_ids,
            **kwargs,
        )

    async def add_reaction(self, *args, message_id: int, code: str, **kwargs) -> None:
        """
        Метод для добавления реакции на сообщение.
        Для добавления реакции вам необходимо знать id сообщения.

        message_id: int - Идентификатор сообщения, на которое добавляется реакция.
        code: str - Emoji символ реакции.
        """
        return await BotMethods.add_reaction(*args, client=self.client,
                                             id=message_id, code=code, **kwargs)

    async def create_task(self, *args, kind: str, content: str = None, due_at: str = None,
                          priority: int = 1, performer_ids: list[int] = None, **kwargs) -> dict:
        """
        Метод для создания новой задачи.

        kind: str - Тип: call (позвонить контакту), meeting (встреча), reminder (напоминание), event (событие),
        email (написать письмо).
        content: str - 	Описание (по умолчанию - название типа).
        due_at: str - Срок выполнения задачи (ISO-8601) в формате YYYY-MM-DDThh:mm:ss.sssTZD. Если указано время 23:59:59.000,
        то задача будет создана на весь день (без указания времени).
        priority: int - Приоритет: 1 (по умолчанию), 2 (важно) или 3 (очень важно).
        performer_ids: list[int] - Массив идентификаторов пользователей, привязываемых к задаче как «ответственные»
        (по умолчанию ответственным назначаетесь вы).
        """

        task_data = TaskData(
            kind=kind,
            content=content,
            due_at=due_at,
            priority=priority,
            performer_ids=performer_ids,
        )
        return await BotMethods.create_task(*args, client=self.client, task_data=task_data, **kwargs)

    async def get_reactions(self, *args, message_id: int, **kwargs) -> dict:
        """
        Метод для получения актуального списка реакций на сообщение.

        Необходимые параметры:

        message_id: int - Идентификатор сообщения, список реакций на которое необходимо получить.

        Количество возвращаемых сущностей за один запрос (по умолчанию 50, максимум 50).

        Страница выборки (по умолчанию 1).
        """
        return await BotMethods.get_reactions(*args, id=message_id, client=self.client, **kwargs)

    async def delete_reaction(self, *args, message_id: int, code: str, **kwargs) -> None:
        """
        Метод для удаления реакции на сообщение.

        Необходимые параметры:

        message_id: int - Идентификатор сообщения, у которого удаляется реакция.

        code: str - Emoji символ реакции.

        """
        return await BotMethods.delete_reaction(
            *args, id=message_id, client=self.client, code=code, **kwargs
        )

    async def create_thread(self, *args, message_id: int, **kwargs) -> None:
        """
        Метод для создания нового треда к сообщению.

        Необходимые параметры:

        message_id: int - Идентификатор сообщения, к которому создается тред.
        """
        return await BotMethods.create_thread(*args, id=message_id, client=self.client, **kwargs)

    async def delete_member_in_chat(self, *args, id: int, member_id: int, **kwargs) -> None:
        """
        Метод для добавления пользователей в состав участников
        беседы или канала.
        Необходимые параметры:

        id: int - Уникальный id беседы или канала.
        member_ids: int - Идентификатор пользователя, который будет удален из беседы или канала.

        """
        return await BotMethods.delete_member_in_chat(*args, client=self.client, id=id, member_id=member_id, **kwargs)

    async def delete_tag_in_chat(self, *args, id: int, group_tag_id: int, **kwargs) -> None:
        """
        Метод для удаление тега в состав участников беседы или канала.
        Необходимые параметры:

        id: int - Идентификатор беседы/канала.
        group_tag_id: int - Идентификатор тега, пользователи которого будут удалены из беседы/канала.

        """
        return await BotMethods.delete_tag_in_chat(*args, client=self.client, id=id, group_tag_id=group_tag_id, **kwargs)
