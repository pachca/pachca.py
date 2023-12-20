URL_TASKS = '/tasks'

TASK = {
    'task': {
        'kind': 'reminder',
        'content': 'Забрать со склада 21 заказ',
        'due_at': '2020-06-05T12:00:00.000+0300',
        'priority': 2
    }
}

TASK_INCORRECT = {
    'task': {
        'content': 'Забрать со склада 21 заказ',
        'due_at': '2020-06-05T12:00:00.000+0300',
        'priority': 2
    }
}

RESPONSE_CREATED_TASK = {
    'data': {
        'id': 22283,
        'kind': 'reminder',
        'content': 'Забрать со склада 21 заказ',
        'due_at': '2020-06-05T09:00:00.000Z',
        'priority': 2,
        'user_id': 12,
        'status': 'undone',
        'created_at': '2020-06-04T10:37:57.000Z',
        'performer_ids': [
          12
        ]
    }
}
