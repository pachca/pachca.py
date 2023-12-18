from session import HttpClient


async def get_users(client: HttpClient):
    return await client.get(endpoint='users/')
