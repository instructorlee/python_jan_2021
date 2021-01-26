food = 'pizza'
response = ''

if food == 'pizza':
    response = 'yummy'

else:
    response = 'i guess I can eat it'

print (response)

subject = 'maths'

print(
    'I LIKE!' if subject == 'science' else "it's OK."
)

print (
    'I LIKE!' if subject == 'science' else 
    "so-so" if subject == 'maths' else 
    'no thank you' if subject == 'english' else 
    "it's OK"
)

