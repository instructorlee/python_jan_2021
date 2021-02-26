import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse

from book_website.decorators import validate_request

from book_manager.models import Book


@validate_request
def add_book_view(request, user):

    post_data = json.loads(request.body.decode("utf-8"))
    errors = Book.objects.validate(post_data)
    if errors:
        return JsonResponse({
            'errors': errors
        }, status=400)

    book = Book.objects.create(owner=user, title=post_data['title'], author=post_data['author'])

    return HttpResponse(json.dumps(json.loads(serializers.serialize('json', [book]))), status=200)


@validate_request
def delete_book_view(request, user, book_id):

    try:
        book = Book.objects.get(id=book_id, owner=user)
        book.delete()
        return HttpResponse(status=201)
    except:
        pass

    return HttpResponse(status=403)


@validate_request
def update_book_view(request, user, book_id):

    try:
        book = Book.objects.get(id=book_id, owner=user)
    except:
        return HttpResponse(status=403)

    post_data = json.loads(request.body.decode("utf-8"))
    errors = Book.objects.validate(post_data)
    if errors:
        return JsonResponse({
            'errors': errors
        }, status=400)

    book.title = post_data.get('title', book.title)
    book.author = post_data.get('author', book.author)
    book.save()

    return HttpResponse(json.dumps(json.loads(serializers.serialize('json', [book]))), status=200)
