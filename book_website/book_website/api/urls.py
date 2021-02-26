from django.urls import path

from .views import add_book_view, delete_book_view, update_book_view

urlpatterns = [
    path('/add_book', add_book_view),
    path('/delete_book/<int:book_id>', delete_book_view),
    path('/update_book/<int:book_id>', update_book_view),
]