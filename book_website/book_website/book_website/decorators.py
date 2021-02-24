from functools import wraps

from django.http import HttpResponse

from books.models import User


def validate_request(func):
    @wraps(func)
    def func_wrapper(request, *args, **kwargs):

        try:
            '''
                Check if the 'user_id' is in the request session
                if it exists, load the user; if not, set user to NULL
            '''
            user = None if 'user_id' not in request.session else User.objects.get(id=request.session['user_id'])

        except Exception as ex:
            print(request.session['user_id'])
            print('boo')

        if user:
            return func(request, user, *args, **kwargs)  # the originally called method + the user object

        return HttpResponse('Unauthorized', status=401)

    return func_wrapper
