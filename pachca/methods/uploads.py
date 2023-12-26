from string import Template

from client import HttpClient, Request
from routers import Router


class UploadsMethods:

    @classmethod
    async def uploads(
        cls, client: HttpClient
    ) -> dict[str, str]:
        request: Request = Router.uploads()
        return await client.make_request(request)

    @classmethod
    async def upload_file(cls, client: HttpClient, file_path: str) -> str:
        request_data = await cls.uploads(client)
        upload_url = request_data.pop('direct_url')
        file_name = file_path.split('/')[-1]
        key = Template(request_data['key']).substitute(filename=file_name)
        with open(file_path, 'rb') as file:
            file_data = file.read()
        request_data['file'] = file_data
        request: Request = Router.upload_file(upload_url)
        request.file_data = request_data
        await client.make_request(request)
        return key
