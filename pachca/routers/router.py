from pachca.routers.chats import ChatsRouter
from pachca.routers.group_tags import GroupTagsRouter
from pachca.routers.messages import MessagesRouter
from pachca.routers.tasks import TasksRouter
from pachca.routers.uploads import UploadsRouter
from pachca.routers.users import UserRouter


class Router(
    ChatsRouter, GroupTagsRouter,
    MessagesRouter, TasksRouter,
    UploadsRouter, UserRouter
):
    pass
