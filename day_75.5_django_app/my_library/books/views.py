import requests
from django.shortcuts import render, redirect
from .models import Book

def search_books(request):
    found_books = []
    # Get the search term from the URL query parameter 'q'
    query = request.GET.get('q')

    if query:
        # Call the Google Books API
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        response = requests.get(url)
        data = response.json()

        # Process the API response
        for item in data.get('items', []):
            info = item.get('volumeInfo', {})
            found_books.append({
                'google_id': item.get('id'),
                'title': info.get('title', 'Not available'),
                'author': ', '.join(info.get('authors', ['Unknown'])),
                'published_date': info.get('publishedDate', 'N/A'),
                'description': info.get('description', 'No description available.'),
                'cover_url': info.get('imageLinks', {}).get('thumbnail', '')
            })

    context = {
        'books': found_books,
        'query': query
    }
    return render(request, 'books/index.html', context)


def save_book(request):
    if request.method == 'POST':
        # Check if the book already exists using its google_id
        google_id = request.POST.get('google_id')
        if not Book.objects.filter(google_id=google_id).exists():
            Book.objects.create(
                google_id=google_id,
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                published_date=request.POST.get('published_date'),
                description=request.POST.get('description'),
                cover_url=request.POST.get('cover_url'),
            )
    # Redirect to the page showing the saved books
    return redirect('my_books')


def my_books(request):
    # Get all books, newest first
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/my_books.html', {'books': books})


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return redirect('my_books')
    return render(request, 'books/edit_book.html', {'book': book})


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('my_books')
