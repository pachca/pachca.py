import os

from pachca.client import HttpClient, Request
from pachca.client.types import File, FileType
from pachca.routers import Router


class UploadsMethods:

    @classmethod
    async def uploads(
        cls, client: HttpClient
    ) -> dict[str, str]:
        request: Request = Router.uploads()
        return await client.make_request(request)

    @classmethod
    async def upload_file(
        cls,
        client: HttpClient,
        file_path: str,
        file_type: FileType
    ) -> str:
        request_data = await cls.uploads(client)

        upload_url = request_data.pop('direct_url')
        file_name = file_path.split('/')[-1]

        request_data['key'] = request_data['key'].replace(r'${filename}', file_name)
        with open(file_path, 'rb') as file:
            request_data['file'] = file.read()

        request: Request = Router.upload_file(upload_url)
        request.file_data = request_data
        await client.make_request(request)

        return File(
            key=request_data['key'],
            name=file_name,
            file_type=file_type,
            size=os.path.getsize(file_path)
        )
