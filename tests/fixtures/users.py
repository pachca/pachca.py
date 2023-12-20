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
USERS_URL = 'users/'
