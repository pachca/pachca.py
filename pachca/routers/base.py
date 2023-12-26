class BaseRouter:

    BASE_URL = 'https://api.pachca.com/api/shared/v1/{postfix}'

    @classmethod
    def _make_endpoint(cls, url) -> str:
        return cls.BASE_URL.format(postfix=url)
