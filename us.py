from typing import Dict

_users = {
    'luap': {
        'name': 'Luap',
        'gender': 'f',
        'city': 'Saint-Petersburg',
        'preferences': 'liquor, party'
    },
    'rec': {
        'name': 'Rec',
        'gender': 'm',
        'city': 'Moscow',
        'preferences': 'brandy, party'
    },
    'busya': {
        'name': 'Busya',
        'gender': 'm',
        'city': 'Saint-Petersburg',
        'preferences': 'Sedova, water'
    },
    'juja': {
        'name': 'Juja',
        'gender': 'f',
        'city': 'Saint-Petersburg',
        'preferences': 'Sedova, toys'
    }
}

_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)


def get_users_by_name(q):
    results = []
    for user in _user_list:
        if q.lower() in user['name'].lower():
            results.append(user)
    return results


def get_user(username):
    return _users.get(username)