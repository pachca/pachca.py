from .chats import ChatsMethods
from .group_tags import GroupTagsMethods
from .messages import MessagesMethods
from .tasks import TasksMethods
from .uploads import UploadsMethods
from .users import UserMethods


class BotMethods(
    ChatsMethods, GroupTagsMethods,
    MessagesMethods, TasksMethods,
    UploadsMethods, UserMethods
):
    pass
