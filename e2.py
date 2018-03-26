users = [
    {'admin' : True, 'active': True, 'name': 'Kevin'},
    {'admin' : False, 'active': True, 'name' : 'David'},
    {'admin' : True, 'active': False, 'name': 'Kevin'},
    {'admin' : False, 'active': False, 'name' : 'David'}
]

line = 1
for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1