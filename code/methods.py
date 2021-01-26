dictionary_example = {
    'key': 'value',
    'name': 'Fred Flintstone',
    'role': 'manager'
}

def build_animal_data(name, dob, country='Africa', is_mammal=True):
    pass

def do_login(username, password=None):
    user_role = 'visitor'
    if password:
        user_role = 'admin'

    return  user_role # ends the function processing