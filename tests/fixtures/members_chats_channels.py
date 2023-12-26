URL_ADD_MEMBERS = '/chats/1/members'

URL_DEL_MEMBERS = '/chats/1/members/1'

URL_ADD_TAGS = '/chats/1/group_tags'

URL_DEL_TAG = '/chats/{id}/group_tags/{id}'

PREPARE_CORRECT_MEMBERS = {'members_ids': [1, 2, 3]}

PREPARE_CORRECT_TAGS = {'group_tag_ids': [86, 18]}

PREPARE_INCORRECT_TAGS = {'group_tag_ids': 1}

PREPARE_INCORRECT_MEMBERS = {'members_ids': [1, 2, 3]}
