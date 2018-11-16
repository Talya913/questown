_users = {
    'Luap': {
        'name': 'Luap',
        'gender': 'f',
        'country': 'Russia',
    },
    'rec': {
        'name': 'Rec',
        'gender': 'm',
        'country': 'USa',
    }
}

def get_user(username):
    return _users.get(username)