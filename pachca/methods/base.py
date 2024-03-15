from pachca.methods.chats import ChatsMethods
from pachca.methods.group_tags import GroupTagsMethods
from pachca.methods.messages import MessagesMethods
from pachca.methods.tasks import TasksMethods
from pachca.methods.uploads import UploadsMethods
from pachca.methods.users import UserMethods


class BotMethods(
    ChatsMethods, GroupTagsMethods,
    MessagesMethods, TasksMethods,
    UploadsMethods, UserMethods
):
    pass
