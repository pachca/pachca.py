from client import HttpClient, Request
from routers import Router


class UploadsMethods:

    @classmethod
    async def get_uploading_unique_params(
        cls, client: HttpClient
    ) -> dict[str, str]:
        request: Request = Router.get_uploading_unique_params()
        return await client.make_request(request)

    @classmethod
    async def upload_file(cls, client: HttpClient, file_path: str) -> str:
        request_data: dict = await cls.get_uploading_unique_params(client)
        upload_url: str = request_data.pop('direct_url')
        file_name: str = file_path.split('/')[-1]
        key: str = request_data['key'].format(filename=file_name)
        with open(file_path, 'rb') as file:
            file_data = file.read()
        request_data['file'] = file_data
        request: Request = Router.upload_file(upload_url)
        request.data = request_data
        await client.make_request(request)
        return key
