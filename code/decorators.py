from functools import wraps


def authenticate_user(func):
    @wraps(func)
    def func_wrapper(user, *args, **kwargs):
        if user['name'] != 'Fred':
            return None

        return func(user)

    return func_wrapper


@authenticate_user
def has_a_popular_cat(user):
    popular_cats = ['Ragdoll', 'British Shorthair', 'Persian', 'Maine Coon']
    return f"{user['name']} {'has' if user['cat_type'] in popular_cats else 'does not have'} a popular cat."


fred = {
    'name': 'Fred',
    'cat_type': 'Siamese'
}

wilma = {
    'name': 'Wilma',
    'cat_type': 'Persian'
}


print(has_a_popular_cat(fred))
print(has_a_popular_cat(wilma))