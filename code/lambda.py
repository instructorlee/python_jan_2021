def add_four(number):
    return number + 4

print(add_four(5))

x = lambda a : a + 7

print (x(8))

things_i_like = {
    'food': 'pizza',
    'animal': 'cat'
}

like = lambda key, item : 'yes' if item == things_i_like[key] else 'no'

print (like('food', 'pizza'))

def like_func(key, item):
    if things_i_like[key] == item:
        return 'yes'
    else:
        return 'no'

print (like_func('animal', 'dog'))