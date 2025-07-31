from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_books, name='search_books'),
    path('save/', views.save_book, name='save_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]