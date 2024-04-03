from pachca.client import HttpClient, Request, RequestData
from pachca.routers import Router


class CustomPropertiesMethods:

    @classmethod
    async def get_custom_properties(cls, client: HttpClient, entity_type, **kwargs):
        request: Request = Router.get_custom_properties()
        request.data = RequestData(entity_type=entity_type).to_dict()
        return await client.make_request(request)
