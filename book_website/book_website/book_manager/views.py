from datetime import datetime
from django.shortcuts import render

HOURS_OF_OPERATION = [
    {'day': 'Monday', 'open': '8am', 'close': '5pm'},
    {'day': 'Tuesday', 'open': '8am', 'close': '5pm'},
    {'day': 'Wednesday', 'open': 'closed', 'close': 'closed'},
    {'day': 'Thursday', 'open': '8am', 'close': '5pm'},
    {'day': 'Friday', 'open': '8am', 'close': '5pm'},
    {'day': 'Saturday', 'open': '8am', 'close': '5pm'},
    {'day': 'Sunday', 'open': 'closed', 'close': 'closed'}
]

# Create your views here.
def index_view(request):

    day_of_week = datetime.today().weekday() # returns a number 0 - 7; 0 = Monday

    context = {
        'todays_hours': HOURS_OF_OPERATION[day_of_week],
        'hours_of_operation': HOURS_OF_OPERATION
    }

    return render(request, 'index.html', context)