LIST_MESSAGES = {
    'data': [
        {
          'id': 1194277,
          'entity_type': 'discussion',
          'entity_id': 198,
          'chat_id': 198,
          'content': 'Это сообщение тоже попадёт в экспорт',
          'user_id': 12,
          'created_at': '2023-09-18T13:43:32.000Z',
          'files': [],
          'thread': {
            'id': 2633,
            'chat_id': 44997
          },
          'parent_message_id': None
        },
        {
          'id': 1194276,
          'entity_type': 'discussion',
          'entity_id': 198,
          'chat_id': 198,
          'content': '**Andrew** добавил **Export bot** в беседу',
          'user_id': 12,
          'created_at': '2023-09-18T13:43:27.000Z',
          'files': [],
          'thread': None,
          'parent_message_id': None
        },
        {
          'id': 1194275,
          'entity_type': 'discussion',
          'entity_id': 198,
          'chat_id': 198,
          'content': '**Andrew** создал беседу',
          'user_id': 12,
          'created_at': '2023-09-18T13:43:19.000Z',
          'files': [],
          'thread': None,
          'parent_message_id': None
        }
    ]
}

INFO_MESSAGES = {
    'data': {
        'id': 194275,
        'entity_type': 'discussion',
        'entity_id': 198,
        'chat_id': 198,
        'content': 'Привет!',
        'user_id': 12,
        'created_at': '2020-06-08T09:32:57.000Z',
        'files': [
            {
                'id': 3560,
                'key': 'attaches/files/12/21zu7934/congrat.png',
                'name': 'congrat.png',
                'file_type': 'file',
                'url': 'https://test.ru'
            }
        ],
        'thread': {
            'id': 29873,
            'chat_id': 1949863
        },
        'parent_message_id': 194274
    }
}

NEW_MESSAGE = {
    'entity_type': 'discussion',
    'entity_id': 198,
    'content': 'Привет!',
}

NEW_MESSAGE_INCORRECT = {
    'entity_type': 'discussion',
    'entity_id': 198,
    'content': 'Привет!',
    'files': 1,
}

RESPONSE_NEW_MESSAGE_DATA = {
    'data': {
        'id': 194275,
        'entity_type': 'discussion',
        'entity_id': 198,
        'chat_id': 198,
        'content': 'Привет',
        'user_id': 12,
        'created_at': '2020-06-08T09:32:57.000Z',
        'files': [],
        'thread': None,
        'parent_message_id': None
    }
}

EDIT_MESSAGE = {
    'message': {
        'content': 'Привет',
        'files': []
    }
}
