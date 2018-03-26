#Exercise #1


user = { 'admin': True, 'active': True, 'name': 'Kevin' }
prefix = ""

if user['admin'] and user['active']:
    prefix = "Admin - Active"
elif user['active']:
    prefix = "Active"
elif user['admin']:
    prefix = "Admin"

print(prefix + user['name'])
