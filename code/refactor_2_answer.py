from datetime import datetime
from dateutil.relativedelta import relativedelta

employees = [
    {
        'name': 'Betty Rubble',
        'role': 'manager',
        'dob': datetime(1980, 1, 12),
        'payrate': 70000,
        'exempt': True
    },
    {
        'name': 'Fred Flintstone',
        'role': 'hr',
        'dob': datetime(1982, 5, 26),
        'payrate': 65000,
        'exempt': False
    },
    {
        'name': 'Barney Rubble',
        'role': 'floor manager',
        'dob': datetime(1975, 3, 17),
        'payrate': 68000,
        'exempt': True
    },
    {
        'name': 'Wilma Flintstone',
        'role': 'cashier',
        'dob': datetime(1985, 10, 15),
        'payrate': 40000,
        'exempt': False
    }
]

def calculate_age(employee):
    return relativedelta(datetime.now(), employee['dob'])

def determine_payrate_exposure(employee):
    return 'not avialable' if employee['exempt'] else employee['payrate']

for employee in employees:

    print (f"{employee['name']} - age: {calculate_age(employee).years} payrate: {determine_payrate_exposure(employee)}")