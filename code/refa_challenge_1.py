students = []

students.append(
    {
        'name': 'Fred',
        'grade': 10,
        'study': 'maths'
    }
)
students.append(
    {
        'name': 'Barney',
        'grade': 11,
        'study': 'education'
    }
)
students.append(
    {
        'name': 'Wilma',
        'grade': 9,
        'study': 'computer science'
    }
)
students.append(
    {
        'name': 'Betty',
        'grade': 10,
        'study': 'maths'
    }
)

high_schoolers = []
jr_high_schoolers = []

for student in students:
    if student['grade'] > 10:
        high_schoolers.append(student)
    else:
        jr_high_schoolers.append(student)

print (high_schoolers)
print ('--')
print (jr_high_schoolers)