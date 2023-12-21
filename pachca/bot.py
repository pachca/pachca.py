import asyncio

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

    async def get_user(self, id: int):
        """
        Метод для получения информации о пользователе.
        Необходимые параметры:

        id: int

        """
        return await BotMethods.get_user_by_id(self.client, id=id)

    async def create_user(self, data):
        """
        Метод для создания пользователя.
        Необходимые параметры:

        data = {
            first_name	string	Имя
            last_name	string	Фамилия
            nickname	string	Имя пользователя
            email	string*	Электронная почта
            phone_number	string	Телефон
            department	string	Подразделение
            role	string	Уровень доступа: admin (администратор),
                user (сотрудник), multi_guest (мульти-гость)
            suspended	boolean	Приостановка доступа
            list_tags	array of strings	Массив тегов, привязываемых к сотруднику
            custom_properties	array of objects	Задаваемые дополнительные поля
            id	integer	Идентификатор поля
            value	string	Устанавливаемое значение
            skip_email_notify	boolean	Пропуск этапа отправки приглашения
                сотруднику (при значении true сотруднику не будет отправлено
                письмо на электронную почту с приглашением создать аккаунт).
                Данный параметр полезен в случае предварительного создания
                аккаунтов сотрудникам перед их входом через SSO.
        }

        """
        return await BotMethods.create_user(self.client, data=data)


async def main(token='YrIvO84kJukmR8J9yrWF2SYApQepMbxDsvRUzZOFTIU'):
    bot = Bot(token)
    response = await bot.get_users()
    print(response)

asyncio.run(main())
