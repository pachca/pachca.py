from .base import BaseRouter


class MessagesRouter(BaseRouter):

    @classmethod
    def get_messages(cls, *args, **kwargs):
        pass

    @classmethod
    def get_message_by_id(cls, *args, **kwargs):
        pass

    @classmethod
    def edit_message(cls, *args, **kwargs):
        pass

    @classmethod
    def add_reaction(cls, *args, **kwargs):
        pass

    @classmethod
    def get_reaction(cls, *args, **kwargs):
        pass

    @classmethod
    def delete_reaction(cls, *args, **kwargs):
        pass

    @classmethod
    def send_messages(cls, *args, **kwargs):
        pass

    @classmethod
    def create_threade(cls, *args, **kwargs):
        pass
