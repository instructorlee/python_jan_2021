from datetime import datetime
from django.shortcuts import render, redirect
from .models import Book, User
from django.contrib import messages

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

    # check if a user is logged in
    user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
    if not user:  # if not, return to index
        return redirect('index')

    if request.method == 'POST':
        errors = Book.objects.validate(request.POST)
        if errors:
            for e in errors.values():
                messages.error(request, e)
            return redirect('/book/add')

        # save the book to dB
        book = Book.objects.create(owner=user, title=request.POST.get('title'), author=request.POST.get('author'))

        messages.add_message(
            request,
            messages.SUCCESS,
            '{} by {} has been added'.format(book.title, book.author))

        return redirect('/exchange')

    else:
        return render(request, 'add_book.html')


def book_view(request):
    # removed check_books_list(request)

    return render(request, 'book.html', {
        'books': Book.objects.all()
    })


def check_books_list(request):
    if 'books' not in request.session:
        request.session['books'] = []


def delete_book_view(request, book_id):
    user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
    if not user:  # if not, return to index
        return redirect('index')

    book = Book.objects.get(id=book_id)
    if book.owner == user:
        book.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            '{} by {} has been deleted'.format(book.title, book.author))
    return redirect('exchange')


def edit_book_view(request, book_id):
    user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
    if not user:  # if not, return to index
        return redirect('index')

    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        if book.owner != user:
            request.session.clear()
            return redirect('index')

        errors = Book.objects.validate(request.POST)

        if errors:
            for e in errors.values():
                messages.error(request, e)
            return redirect(f'/edit/{book_id}')

        book.author = request.POST.get('author', book.author)
        book.title = request.POST.get('title', book.title)
        book.save()

        messages.add_message(request, messages.SUCCESS, 'book updated')

        return redirect('exchange')

    else:
        return render(request, 'edit_book.html', context={'book': Book.objects.get(id=book_id)})


def exchange_view(request):

    user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])
    if not user:  # if not, return to index
        return redirect('index')

    available_books = Book.objects.all().exclude(owner=user).exclude(checked_out_to__isnull=False)
    borrowed_books = Book.objects.filter(checked_out_to=user)

    return render(request, 'exchange_index.html', {
        'user': user,
        'available_books': available_books,
        'borrowed_books': borrowed_books
    })


def index_view(request):
    day_of_week = datetime.today().weekday()
    user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])

    context = {
        'todays_hours': HOURS_OF_OPERATION[day_of_week],
        'hours_of_operation': HOURS_OF_OPERATION,
        'user': user
    }

    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        user = User.objects.authenticate(request.POST.get('email', None), request.POST.get('password', None))
        if user:
            request.session['user_id'] = user.id

            return redirect('index')

        else:
            messages.add_message(request, messages.ERROR, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout_view(request):
    request.session.clear()
    return redirect('index')


def register_view(request):
    errors = User.objects.validate(request.POST)

    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/login')

    else:
        user = User.objects.register(request.POST)

        request.session['user_id'] = user.id

        return redirect('index')


def view_book(request, book_id):
    check_books_list(request)

    # validation
    if book_id > len(request.session['books']) - 1:
        return redirect('/book')

    return render(request, 'view_book.html', {
        'book': request.session['books'][book_id]
    })
