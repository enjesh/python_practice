# Measure some strings:
words = ['cat', 'window', 'defenestrate', 'Elizabeth', 'Rahab']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        print([user])

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        print([user])