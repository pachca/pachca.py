from .chats import ChatsRouter
from .group_tags import GroupTagsRouter
from .messages import MessagesRouter
from .tasks import TasksRouter
from .uploads import UploadsRouter
from .users import UserRouter


class Router(
    ChatsRouter, GroupTagsRouter,
    MessagesRouter, TasksRouter,
    UploadsRouter, UserRouter
):
    pass
