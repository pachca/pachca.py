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

    async def get_user(self, id: int):
        """
        Метод для получения информации о пользователе.
        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_user_by_id(self.client, id=id)

    async def get_group_tags(self):
        return await BotMethods.get_group_tags(self.client)

    async def get_tag_users(self, tag_id):
        return await BotMethods.get_group_tag_users(self.client, tag_id=tag_id)
    
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

    async def create_chat(self, chat: dict):
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

    async def add_members_to_chat(self, member_ids: dict = None):
        """
        Метод для добавления пользователей в состав участников
        беседы или канала.
        Необходимые параметры:

        member_ids: list[int] - Массив идентификаторов пользователей,
                                    которые станут участниками

        """
        return await BotMethods.add_members_to_chat(self.client, member_ids)

    async def add_tags_to_chat(self, group_tag_ids: dict = None):
        """
        Метод для добавления тегов в состав участников беседы или канала.
        Необходимые параметры:

        group_tag_ids: list[int] - Массив идентификаторов тегов,
                                    которые станут участниками

        """
        return await BotMethods.add_tags_to_chat(self.client, group_tag_ids)

    async def create_task(self, task: dict):
        """
        Метод для создания новой задачи.
        """
        return await BotMethods.create_task(self.client, task)
