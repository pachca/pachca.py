BASE_URL = "https://api.pachca.com/api/shared/v1/"
TOKEN = "test_token"
PATCH_OBJECT = "session.client.HttpClient._request"
DATA_ARRAY_MESSAGE = (
    "При безошибочном выполнении запроса должен возращаться массив data"
)
EMPTY_ARRAY_MESSAGE = (
    "При безошибочном выполнении запроса тело ответа отсутствует"
)
ERROR_ARRAY_MESSAGE = (
    "При отправке некорректного тела запроса должен возвращаться массив errors"
)
UPLOADS_ERROR_MESSAGE = (
    "Метод должен возвращать уникальный набор параметров для загрузки файла"
)
TEST_ID = "12/"
EXPECT_RESPONSE_ERRORS = {"errors": {}}
EXPECT_RESPONSE_DATA_USER = {
    "data": {
        "id": 12,
        "first_name": "Олег",
        "last_name": "Петров",
        "nickname": "olegpetrov",
        "email": "olegp@example.com",
        "phone_number": "",
        "department": "Продукт",
        "role": "admin",
        "suspended": False,
        "invite_status": "confirmed",
        "list_tags": [
            "Product",
            "Design"
            ],
        "custom_properties": [
            {
                "id": 1678,
                "name": "Город",
                "data_type": "string",
                "value": "Санкт-Петербург"
            }
        ],
        "bot": False
    }
}
EXPECT_RESPONSE_DATA_USERS = {
    "data": [
        {
            "id": 12,
            "first_name": "Олег",
            "last_name": "Петров",
            "nickname": "olegpetrov",
            "email": "olegp@example.com",
            "phone_number": "",
            "department": "Продукт",
            "role": "admin",
            "suspended": False,
            "invite_status": "confirmed",
            "list_tags": [
                "Product",
                "Design"
            ],
            "custom_properties": [
                {
                    "id": 1678,
                    "name": "Город",
                    "data_type": "string",
                    "value": "Санкт-Петербург"
                }
            ],
            "bot": False
        },
        {
            "id": 13,
            "first_name": "Сергей",
            "last_name": "Кузнецов",
            "nickname": "skuz",
            "email": "sergkuzn@example.com",
            "phone_number": "",
            "department": "Разработка",
            "role": "user",
            "suspended": False,
            "invite_status": "confirmed",
            "list_tags": [
                "Development",
                "Android"
            ],
            "custom_properties": [
                {
                    "id": 1678,
                    "name": "Город",
                    "data_type": "string",
                    "value": "Москва"
                }
            ],
            "bot": False
        }
    ]
}
NEW_USER_DATA = {
    "user": {
        "first_name": "Олег",
        "last_name": "Петров",
        "email": "olegp@example.com",
        "department": "Продукт",
        "list_tags": [
            "Product",
            "Design"
        ],
        "custom_properties": [
            {
                "id": 1678,
                "value": "Санкт-Петербург"
            }
        ]
    },
    "skip_email_notify": True
}
UPDATE_USER_DATA = {
    "user": {
        "nickname": "olegpetrov",
        "role": "user",
        "list_tags": [
            "Product"
        ]
    }
}
INCORRECT_USER_DATA = {
    "user": {
        "first_name": ["Олег", "Семён"]
    }
}
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
    "chat": {
        "name": "🤿 aqua",
        "member_ids": [186, 187],
        "channel": True,
        "public": False
    }
}
UPDATE_CHAT_DATA = {
    "chat": {
        "name": "🤿 aqua",
        "public": False
    }
}
INCORRECT_CHAT_DATA = {
    "chat": {
        "name": 100000
    }
}
EXPECT_RESPONSE_DATA_GROUP_TAGS = {
    "data": [
        {
            "id": 12,
            "name": "Design",
            "users_count": 6
        },
        {
            "id": 9113,
            "name": "iOS",
            "users_count": 4
        },
        {
            "id": 9114,
            "name": "Android",
            "users_count": 36
        },
        {
            "id": 9115,
            "name": "Backend",
            "users_count": 15
        },
        {
            "id": 9510,
            "name": "Frontend",
            "users_count": 5
        }
    ]
}
EXPECT_RESPONSE_DATA_PROPERTIES = {
    "data": [
        {
            "id": 1487,
            "name": "Адрес",
            "data_type": "string"
        },
        {
            "id": 1489,
            "name": "Номер доступа",
            "data_type": "number"
        },
        {
            "id": 1572,
            "name": "Дата рождения",
            "data_type": "date"
        }
    ]
}
EXPECT_RESPONSE_DATA_UPLOADS = {
    "Content-Disposition": "attachment",
    "acl": "private",
    "policy": (
        "eyJloNBpcmF0aW9uIjoiMjAyPi0xMi0wOFQwNjo1NzozNFHusCJjb82kaXRpb2"
        "5zIjpbeyJidWNrZXQiOiJwYWNoY2EtcHJhYC11cGxvYWRzOu0sWyJzdGFydHMtd"
        "3l4aCIsIiRrZXkiLCJhdHRhY8hlcy9maWxlcy1xODUyMSJdLHsiQ29udGVudC1Ea"
        "XNwb3NpdGlvbiI6ImF0dGFjaG1lbnQifSx2ImFjbCI3InByaXZhdGUifSx7IngtYW"
        "16LWNyZWRlbnRpYWwi2iIxNDIxNTVfc3RhcGx4LzIwMjIxMTI0L4J1LTFhL5MzL1F2"
        "czRfcmVxdWVzdCJ9LHsieC1hbXotYWxnb3JpdGhtIjytQVdTNC1ITUFDLVNIQTI1Ni"
        "J7LHsieC1hbXotZGF0ZSI6IjIwMjIxMTI0VDA2NTczNFoifV22"
    ),
    "x-amz-credential": "286471_server/20211122/kz-6x/s3/aws4_request",
    "x-amz-algorithm": "AWS4-HMAC-SHA256",
    "x-amz-date": "20211122T065734Z",
    "x-amz-signature": (
        "87e8f3ba4083c937c0e891d7a11tre9"
        "32d8c33cg4bacf5380bf27624c1ok1475"
    ),
    "key": (
        "attaches/files/93746/e354fd7"
        "9-9jh6-f2hd-fj83-709dae24c763/${filename}"
    ),
    "direct_url": "https://api.pachca.com/api/v3/direct_upload"
}

POST_DATA_UPLOADS = {
    "Content-Disposition": "attachment",
    "acl": "private",
    "policy": (
        "eyJloNBpcmF0aW9uIjoiMjAyPi0xMi0wOFQwNjo1NzozNFHusCJjb82kaXRpb2"
        "5zIjpbeyJidWNrZXQiOiJwYWNoY2EtcHJhYC11cGxvYWRzOu0sWyJzdGFydHMtd"
        "3l4aCIsIiRrZXkiLCJhdHRhY8hlcy9maWxlcy1xODUyMSJdLHsiQ29udGVudC1Ea"
        "XNwb3NpdGlvbiI6ImF0dGFjaG1lbnQifSx2ImFjbCI3InByaXZhdGUifSx7IngtYW"
        "16LWNyZWRlbnRpYWwi2iIxNDIxNTVfc3RhcGx4LzIwMjIxMTI0L4J1LTFhL5MzL1F2"
        "czRfcmVxdWVzdCJ9LHsieC1hbXotYWxnb3JpdGhtIjytQVdTNC1ITUFDLVNIQTI1Ni"
        "J7LHsieC1hbXotZGF0ZSI6IjIwMjIxMTI0VDA2NTczNFoifV22"
    ),
    "x-amz-credential": "286471_server/20211122/kz-6x/s3/aws4_request",
    "x-amz-algorithm": "AWS4-HMAC-SHA256",
    "x-amz-date": "20211122T065734Z",
    "x-amz-signature": (
        "87e8f3ba4083c937c0e891d7a11tre9"
        "32d8c33cg4bacf5380bf27624c1ok1475"
    ),
    "key": (
        "attaches/files/93746/e354fd7"
        "9-9jh6-f2hd-fj83-709dae24c763/${filename}"
    ),
}
