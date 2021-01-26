students = [
    {
        'name': 'Fred',
        'grade': 10,
        'study': 'maths'
    },
    {
        'name': 'Barney',
        'grade': 11,
        'study': 'education'
    },
    {
        'name': 'Wilma',
        'grade': 9,
        'study': 'computer science'
    },

    {
        'name': 'Betty',
        'grade': 10,
        'study': 'maths'
    }
]

high_schoolers = []
jr_high_schoolers = []

for student in students:
    high_schoolers.append(students) if student['grade'] > 10 else jr_high_schoolers.append(student) 

print (high_schoolers)
print ('--')
print (jr_high_schoolers)