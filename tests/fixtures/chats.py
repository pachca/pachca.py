EXPECT_RESPONSE_DATA_CHAT = {
    "data": {
        "id": 12,
        "name": "🤿 aqua",
        "created_at": "2021-08-28T15:56:53.000Z",
        "owner_id": 185,
        "member_ids": [
            185,
            186,
            187
        ],
        "group_tag_ids": [],
        "channel": True,
        "public": False
    }
}
EXPECT_RESPONSE_DATA_CHATS = {
    "data": [
        {
            "id": 12,
            "name": "🤿 aqua",
            "created_at": "2021-08-28T15:56:53.000Z",
            "owner_id": 185,
            "member_ids": [
                185,
                186,
                187
            ],
            "group_tag_ids": [],
            "channel": True,
            "public": False
        },
        {
            "id": 333,
            "name": "development",
            "created_at": "2021-08-28T15:54:22.000Z",
            "owner_id": 185,
            "member_ids": [
                185
            ],
            "group_tag_ids": [
                22,
                24
            ],
            "channel": False,
            "public": True
        }
    ]
}
NEW_CHAT_DATA = {
    "name": "🤿 aqua",
    "member_ids": [186, 187],
    "channel": True,
    "public": False
}
UPDATE_CHAT_DATA = {
    "id": 12,
    "name": "🤿 aqua",
    "public": False
}
INCORRECT_CHAT_DATA = {
    "id": 12,
    "name": 100000
}

NOT_CHAT_DATA = {
    "id": 12,
}
