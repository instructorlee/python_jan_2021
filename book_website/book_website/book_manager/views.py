from datetime import datetime
from django.shortcuts import render, redirect

# 2
HOURS_OF_OPERATION = [
    {'day': 'Sunday', 'open': 'closed', 'close': 'closed'},
    {'day': 'Monday', 'open': '8am', 'close': '5pm'},
    {'day': 'Tuesday', 'open': '8am', 'close': '5pm'},
    {'day': 'Wednesday', 'open': 'closed', 'close': 'closed'},
    {'day': 'Thursday', 'open': '8am', 'close': '5pm'},
    {'day': 'Friday', 'open': '8am', 'close': '5pm'},
    {'day': 'Saturday', 'open': '8am', 'close': '5pm'}
]


def add_book_view(request):

    if request.method == 'POST':
        check_books_list(request)

        # simple data validation
        title = request.POST.get('title', None)  # request.POST['title']
        author = request.POST.get('author', None)

        if not title or not author:
            return redirect(request, '/add_book')

        # save the book
        request.session['books'].append({
            'id': len(request.session['books']),
            'title': title,
            'author': author
        })
        # request.session.save()

        # print(request.session['books'])

        return redirect('/book')  # always redirect after POST

    else:  # is GET request, return the add book HTML
        return render(request, 'add_book.html')


def book_view(request):
    check_books_list(request)

    print(request.session['books'])

    return render(request, 'book.html', {
        'books': request.session['books']
    })


def check_books_list(request):
    if 'books' not in request.session:
        request.session['books'] = []


def index_view(request):
    day_of_week = datetime.today().weekday()  # returns a number 0 - 7; 0 = Monday

    context = {
        'todays_hours': HOURS_OF_OPERATION[day_of_week],
        'hours_of_operation': HOURS_OF_OPERATION
    }

    return render(request, 'index.html', context)


def view_book(request, book_id):
    check_books_list(request)

    # validation
    if book_id > len(request.session['books']) - 1:
        return redirect('/book')

    return render(request, 'view_book.html', {
        'book': request.session['books'][book_id]
    })
